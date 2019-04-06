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

        objects  = p.parsed_result["objects"]
        sections = p.detect_sections()
        # for obj in objects:
        #     print(obj)
        #     #print("obj", str(obj["obj_data"]["ref"]).rjust(5, " "), "|", str(obj["location"]["line_begin"]).rjust(5, " "),"=>", str(obj["location"]["line_end"]).rjust(5, " "))
