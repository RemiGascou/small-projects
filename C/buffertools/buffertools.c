#include "buffertools.h"

int bufferdump(char * buffer, int size) {
    int eos_encountered = 0;
    char c;
    printf("\x1b[1m================================ [BUFFER DUMP] =================================\x1b[0m\x1b[92m\n");
    for (int index = 0; index < size; index++) {
        c = (char)buffer[index];
        if ((char)buffer[index] == '\0') {
            if(eos_encountered == 1){printf("\x1b[1m\x1b[91m");}
            printf("\\0");
            if(!eos_encountered){eos_encountered=1;}
        }
        if (c == '\n') {
            if(eos_encountered == 1){printf("\x1b[1m\x1b[91m");}
            printf("\\n");
            if(eos_encountered == 1){printf("\x1b[0m");}
        } else if (c == '\t') {
            if(eos_encountered == 1){printf("\x1b[1m\x1b[91m");}
            printf("\\t");
            if(eos_encountered == 1){printf("\x1b[0m");}
        } else if (c == '\r') {
            if(eos_encountered == 1){printf("\x1b[1m\x1b[91m");}
            printf("\\r");
            if(eos_encountered == 1){printf("\x1b[0m");}
        } else {
            if(eos_encountered == 1){printf("\x1b[1m\x1b[91m");}
            printf("%c", (char)buffer[index]);
            if(eos_encountered == 1){printf("\x1b[0m");}
        }
    }
    printf("\n\x1b[1m============================= [END OF BUFFER DUMP] =============================\x1b[0m\n");
    return 0;
}


int rst(char * buffer, int size) {
    for (int index = 0; index < size; index++) {
        buffer[index] = '\0';
    }
    return 0;
}

int fill(char * buffer, int size, char c) {
    for (int index = 0; index < size; index++) {buffer[index] = c;}
    return 0;
}
