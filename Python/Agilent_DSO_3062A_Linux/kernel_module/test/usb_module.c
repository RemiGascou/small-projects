#include <linux/module.h>
#include <linux/usb.h>
#include <linux/device.h>

#define USB_IT8951_VENDOR_ID        0x048d  //ITE Vendor ID
#define USB_IT8951_PRODUCT_ID       0x0220

static int it8951_usb_probe(struct usb_interface *interface, const struct usb_device_id *id)
{
    pr_info("test_string 2\n");

    return 0;
}

static void it8951_usb_disconnect(struct usb_interface *interface)
{
    pr_info("Disconnect enter\n");
}

static const struct usb_device_id it8951_usb_devices [] = {
    { USB_DEVICE(USB_IT8951_VENDOR_ID, USB_IT8951_PRODUCT_ID) },
    {},
};
MODULE_DEVICE_TABLE(usb, it8951_usb_devices);

static struct usb_driver it8951_usb_driver_struct = {
    .name        = "it8951_usb",
    .probe       = it8951_usb_probe,
    .disconnect  = it8951_usb_disconnect,
    //.fops        = &skel_fops,
    .id_table    = it8951_usb_devices,
};

static int __init it8951_usb_init(void)
{
    int result;

    pr_info("test_string 1\n");

    result = usb_register(&it8951_usb_driver_struct);
    if (result < 0) {
        pr_err("usb_register failed for the "__FILE__ "driver."
            "Error number %d", result);
        return -1;
    }

    return 0;
}
module_init(it8951_usb_init);

static void __exit it8951_usb_exit(void)
{
    usb_deregister(&it8951_usb_driver_struct);
}
module_exit(it8951_usb_exit);
