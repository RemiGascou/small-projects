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

        obj = p.find_obj_by_ref(12)

        try:
            print(p.stream_to_text(b''.join(obj["obj_data"]["stream"])))
            print()
        except Exception as e:
            print("NOT ZLIB")
