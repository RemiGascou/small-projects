#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : IDAT
# Author             : Remi GASCOU
# Date created       : 05/05/2019
# Date last modified : 05/05/2019
# Python Version     : 3.*

# IDAT Image data

class IDAT(object):
    """docstring for IDAT."""
    def __init__(self,crc=0):
        super(IDAT, self).__init__()
        self._import_zlib = __import__('zlib')

        # CRC 	                4 bytes
        self.crc                = crc

    def load(self, datain):
        """Documentation for load"""
        if type(datain) == str:
            hex_width = ''.join([hex(ord(c))[2:].rjust(2, "0") for c in datain[4:8]])
            print(datain[4:8], hex_width)
            self.set_width(int(hex_width, 16))
            hex_height = ''.join([hex(ord(c))[2:].rjust(2, "0") for c in datain[8:12]])
            self.set_height(int(hex_height, 16))
            self.set_bit_depth(ord(datain[12:13]))
            self.set_color_type(ord(datain[13:14]))
            self.set_compression_method(ord(datain[14:15]))
            self.set_filter_method(ord(datain[15:16]))
            self.set_interlace_method(ord(datain[16:17]))
            self.set_crc(int(''.join([hex(ord(c))[2:].rjust(2, "0") for c in datain[17:21]]), 16))
        elif type(datain) == bytes and len(datain) == 17:
            self.set_width(int(''.join([hex(c)[2:].rjust(2,"0").upper() for c in list(datain[4:8])]), 16))
            self.set_height(int(''.join([hex(c)[2:].rjust(2,"0").upper() for c in list(datain[8:12])]), 16))
            self.set_bit_depth(int(hex(ord(datain[12:13]))[2:].rjust(2,"0").upper(), 16))
            self.set_color_type(int(hex(ord(datain[13:14]))[2:].rjust(2,"0").upper(), 16))
            self.set_compression_method(int(hex(ord(datain[14:15]))[2:].rjust(2,"0").upper(), 16))
            self.set_filter_method(int(hex(ord(datain[15:16]))[2:].rjust(2,"0").upper(), 16))
            self.set_interlace_method(int(hex(ord(datain[16:17]))[2:].rjust(2,"0").upper(), 16))
            self.set_crc(int(hex(ord(datain[17:21]))[2:].rjust(2,"0").upper(), 16))
        elif type(datain) == IDAT:
            self.set_width(datain.get_width())
            self.set_height(datain.get_height())
            self.set_bit_depth(datain.get_bit_depth())
            self.set_color_type(datain.get_color_type())
            self.set_compression_method(datain.get_compression_method())
            self.set_filter_method(datain.get_filter_method())
            self.set_interlace_method(datain.get_interlace_method())
            self.set_crc(datain.get_crc())
        return self

    def update_crc(self):
        """Documentation for update_crc"""
        self.crc = int(hex(self._import_zlib.crc32(bytes(self)[:-4]) & 0xffffffff)[2:], 16)
        return self.crc

    def infos(self):
        """Documentation for infos"""
        out = ""
        out += "width              : " + "0x"+str(hex(self.get_width()))[2:].rjust(2*4, "0") + " : " + str(self.get_width()) + "\n"
        out += "height             : " + "0x"+str(hex(self.get_height()))[2:].rjust(2*4, "0") + " : " + str(self.get_height()) + "\n"
        out += "bit_depth          : " + "0x"+str(hex(self.get_bit_depth()))[2:].rjust(2, "0").ljust(8, " ") + " : " + str(self.get_bit_depth()) + "\n"
        out += "color_type         : " + "0x"+str(hex(self.get_color_type()))[2:].rjust(2, "0").ljust(8, " ") + " : " + str(self.get_color_type()) + "\n"
        out += "compression_method : " + "0x"+str(hex(self.get_compression_method()))[2:].rjust(2, "0").ljust(8, " ") + " : " + str(self.get_compression_method()) + "\n"
        out += "filter_method      : " + "0x"+str(hex(self.get_filter_method()))[2:].rjust(2, "0").ljust(8, " ") + " : " + str(self.get_filter_method()) + "\n"
        out += "interlace_method   : " + "0x"+str(hex(self.get_interlace_method()))[2:].rjust(2, "0").ljust(8, " ") + " : " + str(self.get_interlace_method()) + "\n"
        out += "crc                : " + "0x"+str(hex(self.get_crc()))[2:].rjust(2*4, "0") + " : " + str(self.get_crc()) + "\n"
        return out

    def __str__(self):
        hex_IDAT  = ""
        hex_IDAT += hex(self.width)[2:][:4].rjust(2*4,"0")
        hex_IDAT += hex(self.height)[2:][:4].rjust(2*4,"0")
        hex_IDAT += hex(self.bit_depth)[2:][:1].rjust(2*1,"0")
        hex_IDAT += hex(self.color_type)[2:][:1].rjust(2*1,"0")
        hex_IDAT += hex(self.compression_method)[2:][:1].rjust(2*1,"0")
        hex_IDAT += hex(self.filter_method)[2:][:1].rjust(2*1,"0")
        hex_IDAT += hex(self.interlace_method)[2:][:1].rjust(2*1,"0")
        hex_IDAT += hex(self.crc)[2:][:2*4].rjust(2*4,"0")
        out = ''.join([chr(int(hex_IDAT[2*k:2*(k+1)], 16)) for k in range(len(hex_IDAT)//2)])
        return "IDAT"+out

    def __bytes__(self):
        hex_IDAT  = ""
        hex_IDAT += hex(self.width)[2:][:2*4].rjust(2*4,"0")
        hex_IDAT += hex(self.height)[2:][:2*4].rjust(2*4,"0")
        hex_IDAT += hex(self.bit_depth)[2:][:2*1].rjust(2*1,"0")
        hex_IDAT += hex(self.color_type)[2:][:2*1].rjust(2*1,"0")
        hex_IDAT += hex(self.compression_method)[2:][:2*1].rjust(2*1,"0")
        hex_IDAT += hex(self.filter_method)[2:][:2*1].rjust(2*1,"0")
        hex_IDAT += hex(self.interlace_method)[2:][:2*1].rjust(2*1,"0")
        hex_IDAT += hex(self.crc)[2:][:2*4].rjust(2*4,"0")
        out = b"IDAT"+bytes([int(hex_IDAT[2*k:2*(k+1)], 16) for k in range(len(hex_IDAT)//2)])
        return out

    # *----------------------------------Get Set---------------------------------- *

    def get_width (self):
        return self.width

    def set_width (self, width):
        self.width = width
        self.update_crc()
        return self

    def get_height (self):
        return self.height

    def set_height (self, height):
        self.height = height
        self.update_crc()
        return self

    def get_bit_depth (self):
        return self.bit_depth

    def set_bit_depth (self, bit_depth):
        self.bit_depth = bit_depth
        self.update_crc()
        return self

    def get_color_type (self):
        return self.color_type

    def set_color_type (self, color_type):
        self.color_type = color_type
        self.update_crc()
        return self

    def get_compression_method (self):
        return self.compression_method

    def set_compression_method (self, compression_method):
        self.compression_method = compression_method
        self.update_crc()
        return self

    def get_filter_method (self):
        return self.filter_method

    def set_filter_method (self, filter_method):
        self.filter_method = filter_method
        self.update_crc()
        return self

    def get_interlace_method (self):
        return self.interlace_method

    def set_interlace_method (self, interlace_method):
        self.interlace_method = interlace_method
        self.update_crc()
        return self

    def get_crc (self):
        return self.crc

    def set_crc (self, crc):
        self.crc = crc
        return self




if __name__ == '__main__':
    i = IDAT()
    print(bytes(i))
    print(i.infos())

    n = IDAT().load(i)
    n.update_crc()
    print(bytes(n))
    print(n.infos())
