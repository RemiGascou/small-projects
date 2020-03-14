// Dynamically allocate char driver major/minor numbers
if((retcode=alloc_chrdev_region(&dev, // First major/minor number to use
    0, // First minor number
    USBTMC_MINOR_NUMBERS, // Number of minor numbers to reserve
    "USBTMCCHR" // Char device driver name
    ))) {
    printk(KERN_ALERT "USBTMC: Unable to allocate major/minor numbers\n");
    goto exit_alloc_chrdev_region;
}

// This structure is used to publish the char device driver functions
static struct file_operations fops = {
    .owner      = THIS_MODULE,
    .read       = usbtmc_read,
    .write      = usbtmc_write,
    .open       = usbtmc_open,
    .release    = usbtmc_release,
    .ioctl      = usbtmc_ioctl,
    .llseek     = usbtmc_llseek,
};

// Initialize cdev structure for this character device
cdev_init(&cdev, &fops);
cdev.owner = THIS_MODULE;
cdev.ops   = &fops;

// Combine major and minor numbers
printk(KERN_NOTICE "USBTMC: MKDEV\n");
devno = MKDEV(MAJOR(dev),n);

// Add character device to kernel list
printk(KERN_NOTICE "USBTMC: CDEV_ADD\n");

if((retcode = cdev_add(&cdev,devno,1))) {
    printk(KERN_ALERT "USBTMC: Unable to add character device\n");
    goto exit_cdev_add;
}
