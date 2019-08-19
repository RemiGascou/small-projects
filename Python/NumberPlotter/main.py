#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from lib import *

def e(x):
    """Documentation for e"""
    return x

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
