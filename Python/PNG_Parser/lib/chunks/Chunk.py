#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : Chunk
# Author             : Remi GASCOU
# Date created       : 05/05/2019
# Date last modified : 05/05/2019
# Python Version     : 3.*

class Chunk(object):
    """docstring for Chunk."""
    def __init__(self,crc=0):
        super(Chunk, self).__init__()

        self._import_zlib = __import__('zlib')
        
        # CRC 	                4 bytes
        self.crc                = crc

    def update_crc(self):
        """Documentation for update_crc"""
        self.crc = int(hex(self._import_zlib.crc32(bytes(self)[:-4]) & 0xffffffff)[2:], 16)
        return self.crc
