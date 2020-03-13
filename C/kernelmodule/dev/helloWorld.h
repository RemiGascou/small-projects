#ifndef HELLOWORLD_H
#define HELLOWORLD_H
#include <linux/ioctl.h>

// cmd ‘KE_DATA_VAR’ to send the integer type data
#define KE_DATA_VAR _IOR('q', 1, int *)

#endif
