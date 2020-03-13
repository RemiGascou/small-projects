#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import os
import sys

chunk_size = 30

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" file")
    else :
        file = sys.argv[1]
        b64data = os.popen("cat "+file+" | base64 | tr -d \"\\n\"").read()
        chunks  = [b64data[chunk_size*k:chunk_size*(k+1)] for k in range(len(b64data)//chunk_size)]+[b64data[chunk_size*(len(b64data)//chunk_size):]]
        for c in chunks:
            print("echo \""+c+"\" >> e.b64;")
        print("cat e.b64 | base64 -d > "+file+";")
