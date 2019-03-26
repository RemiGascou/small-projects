# -*- coding: utf-8 -*-

import sys
from lib import *

def usage():
    print("python3 list_objects.py file.pdf")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    else:
        p = PDF_Parser(sys.argv[1])

        sections = p.detect_sections()

        maxkeylen = max([len(key) for key in sections.keys()])
        maxbeginlen = max([len(str(sections[key]["begin"])) for key in sections.keys()])
        maxendlen   = max([len(str(sections[key]["end"])) for key in sections.keys()])
        headerlen = (maxkeylen+3+maxbeginlen+5+maxendlen+2)

        print("\x1b[1m"+" Structure ".center(headerlen, "=")+"\x1b[0m")
        print(" "*(maxkeylen+1)+"|"+"begin".center((maxbeginlen+2), " ")+" | "+"end".center((maxbeginlen+2), " ")+"|")
        print("="*headerlen)

        for sk in sections.keys():
            print(
                sk.rjust(maxkeylen, " "),
                ":",
                str(sections[sk]["begin"]).rjust(5, " "),
                "==>",
                str(sections[sk]["end"]).rjust(5, " "),
                "|"
            )

        print("\x1b[1m"+"".center(headerlen, "=")+"\x1b[0m")
