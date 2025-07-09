/*
  amisc.c

A driver for a misc device. The device number is 10 n, where n
is dynamically assigned and is reported in /proc/misc
*/

#include <linux/module.h>
#include <linux/init.h>
#include <linux/miscdevice.h>
#include <linux/fs.h>
#include <linux/uaccess.h>

MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("A misc device module");
MODULE_AUTHOR("Me");

static char *readstring = "This is a string.\n";

ssize_t amisc_read(struct file *f,
	char __user *buf, size_t size, loff_t *offset) {
	int res;

	// printk("amisc read: size=%d offset=%lld\n", size, *offset);

	if (size == 0 || *offset > strlen(readstring))
		return 0;

	if ((*offset) + size > strlen(readstring))
		size = strlen(readstring) - *offset;
	res = copy_to_user(buf, readstring + *offset, size);
	if(res)
		return -EFAULT;
	(*offset) += size;

	return size;
}

static struct file_operations fops = {
	.owner = THIS_MODULE,
	.read = amisc_read
};

static struct miscdevice misc;

static int __init amisc_init(void) {
	int res;

	// printk("amisc init\n");
	misc.minor = MISC_DYNAMIC_MINOR;	// check /proc/misc
	misc.name = "amisc";
	misc.fops = &fops;
	res = misc_register(&misc);
	// printk("minor: %d\n", misc.minor);

	return res;
}

static void __exit amisc_exit(void) {
	misc_deregister(&misc);
	// printk("amisc exit\n");
}

module_init(amisc_init);
module_exit(amisc_exit);
