#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : PNG
# Author             : Remi GASCOU
# Date created       : 05/05/2019
# Date last modified : 05/05/2019
# Python Version     : 3.*

from .chunks import *

class PNG(object):
    """docstring for PNG."""
    def __init__(self, filename="", log=True):
        super(PNG, self).__init__()
        self.log         = log
        self.filename    = filename
        self.chunksnames = ["IHDR","PLTE","IDAT","IEND",
            "bKGD","cHRM","gAMA","hIST",
            "pHYs","sBIT","tEXt","tIME",
            "tRNS","zTXt"
        ]

        self.rawdata, self.chunks = [], []
        if self.filename != "" :
            self.readfile(self.filename)
            self.parse()


    def parse(self):
        """Documentation for parse"""
        def addchunk(chkname, buffer):
            """Documentation for new_function"""
            if chkname == "IHDR":
                self.chunks.append(IHDR().load(bytes(buffer)))
            elif chkname == "PLTE":
                pass
            elif chkname == "IDAT":
                pass
            elif chkname == "IEND":
                pass
            elif chkname == "bKGD":
                pass
            elif chkname == "cHRM":
                pass
            elif chkname == "gAMA":
                pass
            elif chkname == "hIST":
                pass
            elif chkname == "pHYs":
                pass
            elif chkname == "sBIT":
                pass
            elif chkname == "tEXt":
                pass
            elif chkname == "tIME":
                pass
            elif chkname == "tRNS":
                pass
            elif chkname == "zTXt":
                pass
            return None
        # ===================================================
        if self.log : print("[LOG] Parsing rawdata ...")
        chunksnames = {'.'.join([str(ord(c)) for c in chk]) : chk for chk in self.chunksnames}

        cnbuffer, buffer, sp = "0.0.0.0", [], []
        for c in self.rawdata:
            cnbuffer = '.'.join([str(e) for e in cnbuffer.split(".")[1:]+[str(c)]])
            if cnbuffer in chunksnames or cnbuffer == ''.join([str(ord(c)) for c in "PNG"]):
                chkname = chunksnames[cnbuffer]
                if self.log: print("[PARSING] Found "+chkname+" lenght "+str(len(buffer)))
                addchunk(chkname, buffer)
                buffer = [c]
            else:
                buffer.append(c)
        if len(buffer) != 0:
            addchunk(chkname, buffer)
        return self.chunks

    def readfile(self, filename):
        if self.log : print("[LOG] Reading file "+filename)
        self.rawdata, self.chunks = [], []
        f = open(filename, "rb")
        data = b''.join(f.readlines())
        f.close()
        self.rawdata = data
        return data

    def writefile(self, filename):
        if self.log : print("[LOG] Writing file "+filename)
        f = open(filename, "wb")
        for e in self.rawdata:
            f.write(e)
        f.close()

    # *----------------------------------Get Set---------------------------------- *

    def get_filename (self):
        return self.filename

    def set_filename (self, filename):
        if type(self.filename) == type(filename):
            self.filename = filename
        return self

    def get_log (self):
        return self.log

    def set_log (self, log):
        if type(self.log) == type(log):
            self.log = log
        return self
