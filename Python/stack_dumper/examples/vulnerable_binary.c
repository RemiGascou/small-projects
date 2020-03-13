#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

char out_buffer[1024]; //Dans BSS

void vuln_format(char * in_buffer, char * out_buffer){
    char * dumb   = "A string in vuln_format(...)";
    sprintf(out_buffer, in_buffer);
}

int main(int argc, char const *argv[]) {
    char * dumb   = "A string in main(...)";
    char * dumb_1 = "TOUM, TOUM, TOUM";
    char * dumb_2 = "Another one bites the dust !";
    char * dumb_3 = "C'est cool mon petit tool quand meme";
    if (argc != 2) {
        printf("Usage : %s PAYLOAD\n", argv[0]);
    } else {
        sprintf(out_buffer, argv[1]);
        printf(out_buffer);
    }
    return 0;
}
