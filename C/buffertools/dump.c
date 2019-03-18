#include <stdio.h>
#include <string.h>
#include "buffertools.h"

int main(int argc, char const *argv[]) {
    int bufferSize = 1024;
    char buffer[bufferSize];
    strcpy(buffer, "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.");
    bufferdump(buffer, bufferSize);
    return 0;
}
