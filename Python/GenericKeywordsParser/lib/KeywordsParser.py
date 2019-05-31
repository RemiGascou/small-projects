#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : KeywordsParser
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from .graph import *
import json

class KeywordsParser(object):
    """docstring for KeywordsParser."""

    def __init__(self, kws, log=False):
        super(KeywordsParser, self).__init__()
        self.log = log
        self.kws = kws
        self.pg  = {}
        self._prepare()

    def _prepare(self, log=False):
        """Documentation for _prepare"""
        log = log or self.log
        self.pg  = {}
        for kw in self.kws:
            buffer, k = self.pg, 0
            for c in kw:
                k += 1
                if c not in buffer.keys():
                    if k == len(kw): buffer[c] = None
                    else:            buffer[c] = {}
                buffer = buffer[c]
        if log : print("===============================")
        if log : print(  json.dumps(self.pg, indent=4)  )
        if log : print("===============================")
        return self.pg



    def parse(self, rawdata, log=False):
        """Documentation for parse"""
        log = log or self.log
        def _iskw(pg,skw, log=False):
            """Documentation for _iskw"""
            buffer, matched, k = pg, [], 0
            for c in skw:
                k += 1
                if buffer != None:
                    if c in buffer.keys():
                        if log : print("  | "+c+" -> Next")
                        matched.append(c)
                        buffer = buffer[c]
                    else:
                        return [False, matched]
                else : #Reached the end
                    if log : print("  | "+c+" -> END")
                    return [True, matched]
            return [False, matched]
        #=========================================
        maxlen = max([len(kw) for kw in self.kws])

        kwbuffer, buffer, before = "", "", ""

        for k in range(len(rawdata)):
            c = rawdata[k]
            kwbuffer = kwbuffer[-maxlen:] + c

            r = _iskw(self.pg, kwbuffer)
            if r[0] == True :
                print("[LOG] Found",''.join(r[1]))
                print(buffer)
                buffer = c
            else:
                buffer += c
        return
