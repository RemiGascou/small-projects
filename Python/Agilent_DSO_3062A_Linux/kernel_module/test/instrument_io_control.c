#include <stdio.h>
#include <fcntl.h>

int main(int argc, char const *argv[]) {
    int myfile;
    char buffer[4000];
    int actual;
    myfile = open("/dev/usbtmc1",O_RDWR);
    if(myfile > 0) {
        write(myfile,"*IDN?\n",6);
        actual = read(myfile,buffer,4000);
        buffer[actual] = 0;
        printf("Response:\n%s\n",buffer);
        close(myfile);
    }
    return 0;
}
