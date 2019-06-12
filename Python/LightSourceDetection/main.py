#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from lib import *

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" imagefile")
    else :
        imagefile = sys.argv[1]
        ld = LightDetector(imagefile)
        ld.find_lightsources().export()
