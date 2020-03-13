#include <stdio.h>
#include <stdlib.h>

char * itonl(long int number) {
    char bit_0 = ' ';
    char bit_1 = '\t';
    unsigned int k = 0;
    unsigned int textsize = 1;
    if (number == 0) { textsize = 1; }
    else             { while ((number >> textsize) != 0) {textsize++;} }
    char * text = malloc(textsize*sizeof(char));
    k = 0;
    do {
        // printf("  | %d => ", number);
        if ( (number & 1) == 1 ) { text[textsize-1-k] = bit_1; }
        else                     { text[textsize-1-k] = bit_0; }
        // printf("text : %s\n", text);
        number = number >> 1; k++;
    } while (number != 0 && k <= textsize);
    return text;
}

int nltoi(char * text) {
    char bit_0 = ' ';
    char bit_1 = '\t';
    unsigned int k = 0;
    unsigned int textsize = 0;
    while (text[k] != '\0') {textsize++; k++;}
    long int parsed_number = 0;
    k = 0;
    while (text[k] != '\0') {
        if ((text[k] != bit_0) && (text[k] != bit_1)) {
            printf("ERROR : Non whitespace caracters encountered at char %d.\n", k);
            return -1;
        }
        else if (text[k] == bit_1) { parsed_number += (1 << (textsize-1-k)); }
        else if (text[k] == bit_0) { }
        k++;
    }
    return parsed_number;
}

/*
int main(int argc, char const *argv[]) {
    unsigned short result = 0;
    for (int i = 0; i <= 9999; i++) {
        printf("\r[%04d] ", i);
        result = (i == nltoi(itonl(i)));
        if (result == 1) {
            printf("\x1b[1;92mPASSED\x1b[0m");
        } else {
            printf("\x1b[1;91mFAILED\x1b[0m\n");
        }
    }
    printf("\n");
    return 0;
}
*/
