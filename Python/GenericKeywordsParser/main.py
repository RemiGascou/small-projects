#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from lib import *

if __name__ == '__main__':
    kw   = ["TEST","NUL","ABCD","HEY","123AZ"]
    data = "..TEST.NUL......ABCD.HEYYYY...ABCD.COUCOU"
    kwp  = KeywordsParser(kw)
    kwp.parse(data)
