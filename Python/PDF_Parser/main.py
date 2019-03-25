# -*- coding: utf-8 -*-

from lib import *

if __name__ == '__main__':
    p = PDF_Parser("pdf_examples/out.pdf")

    print(p.find_obj_by_ref(78, log=True))
