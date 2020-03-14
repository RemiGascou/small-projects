#include <linux/init.h>
#include <linux/module.h>
#include <linux/usb.h>
#include <linux/device.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <asm/uaccess.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Remi GASCOU");
MODULE_DESCRIPTION("Agilent DSO 3000 X Series USB");
MODULE_VERSION("0.2");

#define DEVICE_NAME "agilent_dso_3000_usb"
#define MSG_BUFFER_LEN 1024

#define USB_AGILENT_DSO_3000_VENDOR_ID        0x0400 // Agilent Technologies
#define USB_AGILENT_DSO_3000_PRODUCT_ID       0xc55d // DSO 3000 X Series

// Prototypes for device functions
static int device_open(struct inode *, struct file *);
static int device_release(struct inode *, struct file *);
static ssize_t device_read(struct file *, char *, size_t, loff_t *);
static ssize_t device_write(struct file *, const char *, size_t, loff_t *);
static int agilent_dso_3000_usb_probe(struct usb_interface *interface, const struct usb_device_id *id);
static void agilent_dso_3000_usb_disconnect(struct usb_interface *interface);

// This structure points to all of the device functions
static struct file_operations file_ops = {
    .owner   = THIS_MODULE,
    .read    = device_read,
    .write   = device_write,
    .open    = device_open,
    .release = device_release
};

static const struct usb_device_id agilent_dso_3000_usb_devices [] = {
    { USB_DEVICE(USB_AGILENT_DSO_3000_VENDOR_ID, USB_AGILENT_DSO_3000_PRODUCT_ID) },
    {},
};

MODULE_DEVICE_TABLE(usb, agilent_dso_3000_usb_devices);

static struct usb_driver usb_driver_struct = {
    .name        = "agilent_dso_3000_usb",
    .probe       = agilent_dso_3000_usb_probe,
    .disconnect  = agilent_dso_3000_usb_disconnect,
    //.fops        = &file_ops,
    .id_table    = agilent_dso_3000_usb_devices,
};



// [CHAR Device] ===============================================================

static int major_num;
static int device_open_count = 0;
static char msg_buffer[MSG_BUFFER_LEN];
static char * msg_ptr;

// When a process reads from our device, this gets called.
static ssize_t device_read(struct file * flip, char * buffer, size_t len, loff_t * offset) {
    int bytes_read = 0;

    // If we're at the end, loop back to the beginning
    if (*(msg_ptr) == 0) { msg_ptr = msg_buffer; }

    // Put data in the buffer
    while (len && *(msg_ptr)) {
        // Buffer is in user data, not kernel, so you can't just reference
        // with a pointer. The function put_user handles this for us
        put_user(*(msg_ptr++), buffer++);
        len--;
        bytes_read++;
    }
    return bytes_read;
}

// Called when a process tries to write to our device
static ssize_t device_write(struct file * flip, const char * buffer, size_t len, loff_t * offset) {
    int result = 0;
    struct urb * urb = 0;

    urb = usb_alloc_urb(
        1,          // Number of ISO Packets
        GFP_USER    // Memory flags
    );

    /* we can only write as much as 1 urb will hold */
    unsigned int bytes_written = (count > urb->bulk_out_size) ? urb->bulk_out_size : count;

    /* copy the data from user space into our urb */
    copy_from_user(
        urb->write_urb->transfer_buffer,
        buffer,
        bytes_written
    );

    /* set up our urb */
    // void usb_fill_control_urb(
    //     struct urb *urb,
    //     struct usb_device *dev,
    //     unsigned int pipe,
    //     unsigned char *setup_packet,
    //     void *transfer_buffer,
    //     int buffer_length,
    //     usb_complete_t complete,
    //     void *context
    // );
    // void usb_fill_bulk_urb(struct urb * urb, struct usb_device * dev, unsigned int pipe, void * transfer_buffer, int buffer_length, usb_complete_t complete_fn, void * context)
    usb_fill_bulk_urb(
        urb->write_urb,
        urb->dev,
        usb_sndbulkpipe(
            urb->dev,
            urb->bulk_out_endpointAddr
        ),
        urb->write_urb->transfer_buffer,
        bytes_written,
        skel_write_bulk_callback,
        skel
    );

    /* send the data out the bulk port */
    result = usb_submit_urb(urb->write_urb);
    if (result) { printk(KERN_INFO "Failed submitting write urb, error %d", result); }
    return -EINVAL;
}

// Called when a process opens our device
static int device_open(struct inode * inode, struct file * file) {
    // If device is open, return busy
    if (device_open_count) {
        return -EBUSY;
    }
    device_open_count++;
    try_module_get(THIS_MODULE);
    return 0;
}

// Called when a process closes our device
static int device_release(struct inode * inode, struct file * file) {
    // Decrement the open counter and usage count. Without this, the module would not unload.
    device_open_count--;
    module_put(THIS_MODULE);
    return 0;
}


// [USB Device] ================================================================

static int agilent_dso_3000_usb_probe(struct usb_interface *interface, const struct usb_device_id *id) {
    printk(KERN_INFO "agilent_dso_3000 : Device connected\n");
    return 0;
}

static void agilent_dso_3000_usb_disconnect(struct usb_interface *interface) {
    printk(KERN_INFO "agilent_dso_3000 : Device Disconnected\n");
}


// [Init + exit] ===============================================================

static int __init agilent_dso_3000_usb_init(void) {
    //Register USB Device
    int result = usb_register(&usb_driver_struct);
    if (result < 0) {
        pr_err("usb_register failed for the "__FILE__ "driver."
            "Error number %d", result);
        return -1;
    }

    // Try to register character device
    major_num = register_chrdev(0, DEVICE_NAME, &file_ops);
    if (major_num < 0) {
        printk(KERN_ALERT "Could not register device: %d\n", major_num);
        return major_num;
    } else {
        printk(KERN_INFO "Loaded \x1b[1;93m" DEVICE_NAME "\x1b[0m module, with device major number \x1b[95m%d\x1b[0m\n", major_num);
        return 0;
    }
}

static void __exit agilent_dso_3000_usb_exit(void) {
    // Remember - we have to clean up after ourselves. Unregister the character device.
    usb_deregister(&usb_driver_struct);
    unregister_chrdev(major_num, DEVICE_NAME);
    printk(KERN_INFO "Unloaded \x1b[1;93m" DEVICE_NAME "\x1b[0m module, with device major number \x1b[95m%d\x1b[0m\n", major_num);
}

// Register module functions
module_init(agilent_dso_3000_usb_init);
module_exit(agilent_dso_3000_usb_exit);
