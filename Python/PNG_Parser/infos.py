#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : PNGParser
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from lib import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" image.png")
    else :
        i = IHDR()
        i.load(b'\x00\x00\x02\x80\x00\x00\x01\xe0\x08\x06\x00\x00\x00\x35\xd1\xdc\xe4\x00\x00\x00\x06')
        print(i.infos())
