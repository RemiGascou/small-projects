# -*- coding: utf-8 -*-

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

        print("[LOG] Parsing ...")
        hp = HTMLParser(html)
        p  = hp.parse(log=False)

        print("[LOG] Autoindent ...")
        indented = hp.autoindent()

        print("[LOG] Writing indented_"+filein,"...")
        f = open("indented_"+filein, "w")
        for line in indented:
            f.write(line+"\n")
        f.close()
