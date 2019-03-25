# -*- coding: utf-8 -*-

from malb_mmap import *

if __name__ == '__main__':
    malbmem = malb_mmap()
    malbmem.printmem()
    malbmem[0] = 12
    malbmem.printmem()
