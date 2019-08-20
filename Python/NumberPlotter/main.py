#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from lib import *

def isPrime(n):
    if n<= 1 :
        return False
    else :
        for k in range(2,int(n**(0.5)+1)):
            if n % k == 0:
                return False
        return True
        
def e(x):
    """Documentation for e"""
    return int(isPrime(x))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" DATALEN ROWN")
    else :
        datalen = int(sys.argv[1])
        rown    = int(sys.argv[2])

        cm = ColorMap().current()

        i = ImgPlotter(size=(rown, 0))
        i.set_colormap(cm)
        i.gendata(datalen, modifier=e)
        i.createimg("out.bmp")
