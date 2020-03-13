#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import os, sys
import base64

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    for e in data:
        f.write(e)
    f.close()
    return data

chunk_size = 30

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" file")
    else :
        file = sys.argv[1]
        b64data = os.popen("cat "+file+" | base64 | tr -d \"\\n\"").read()
        print(b64data)
        print("===============")

        f = open(file, "rb")
        data = b'\n'.join(f.readlines())
        f.close()
        bd = base64.b64encode(data).decode("ISO-8859-1")
        print(bd)
        print(b64data == bd)
