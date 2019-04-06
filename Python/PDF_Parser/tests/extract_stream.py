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

        obj = p.find_obj_by_ref(77, log=True)

        print()
        r = p.stream_to_text(b''.join(obj["obj_data"]["stream"]))
        f = open("extracted", "wb")
        f.write(r)
        f.close()
