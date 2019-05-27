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
        image = sys.argv[1]
        png   = PNG(image)
