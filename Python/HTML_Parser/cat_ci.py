#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from lib import *

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 main.py test.html")
    else:
        filein = sys.argv[1]
        print("[LOG] Reading",filein,"...")
        f = open(filein, "r")
        html = '\n'.join(f.readlines())
        f.close()

        print("[LOG] Autoindent ...")
        indented = HTML_Indenter(html).autoindent_colored()
        print(indented)
