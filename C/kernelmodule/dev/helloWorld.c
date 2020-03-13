#include <stdio.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/ioctl.h>
#include <stdlib.h>
#include "helloWorld.h"

/* @brief: function to load the kernel module */
void load_KE() {
    printf ("loading KE\n");
    if (system ("insmod /root/helloWorld.ko") == 0)     {
        printf ("KE loaded successfully");
    }
}

/* @brief: function to unload the kernel module */
void unload_KE() {
    printf ("unloading KE\n");
    if (system ("rmmod /root/helloWorld.ko") == 0)     {
        printf ("KE unloaded successfully");
    }
}

/* @brief: method to send data to kernel module */
void send_data(int fd) {
    int value = 0;
    printf("Enter value: ");
    scanf("%d", &value);
    getchar();
    if (ioctl(fd, KE_DATA_VAR, &value) == -1) {
        perror("send data error at ioctl");
    }
}

int main(int argc, char *argv[]) {
    const char * file_name = "/dev/char_device"; //used by ioctl
    int fd = -1;
    enum {
        e_load,     // load the kernel module
        e_unload,   // unload the kernel module
        e_send,     // send a HB from test binary to kernel module
    } option;

    if (argc == 2) {
        if (strcmp(argv[1], "-l") == 0) {
            option = e_load;
        } else if (strcmp(argv[1], "-u") == 0) {
            option = e_unload;
        }
    } else if (strcmp(argv[1], "-s") == 0) {
        option = e_send;
    } else {
        fprintf(stderr, "Usage: %s [-l | -u | -s ]\n", argv[0]);
        return 1;
    }
}
