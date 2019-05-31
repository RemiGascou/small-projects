#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import time
from lib import *


def tb(kws, data):
    """Documentation for tb"""
    print("================= TEST =================")
    print("Keywords :", len(kws))
    print("Data len :", len(data))
    print("========================================")
    start = time.clock()
    #===========================
    kwp  = KeywordsParser(kws)
    kwp.parse(data)
    #===========================
    tel = round(time.clock() -start, 4)
    print("========================================")
    print("Elapsed time", tel)
    print("=============== END TEST ===============")
    return tel

if __name__ == '__main__':
    kws  = ["TEST","NUL","ABCD","HEY","123AZ"]
    data = "..TEST.NUL......ABCD.HEYYYY...ABCD.COUCOU"
    tb(kws, data)
