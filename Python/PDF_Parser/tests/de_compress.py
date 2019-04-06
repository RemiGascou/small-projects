# -*- coding: utf-8 -*-

import sys
import zlib

if __name__ == '__main__':
    text = b"let's compress some text"
    o_decompressor  = zlib.decompressobj()
    o_compress      = zlib.compressobj()
    print(zlib.compress(text))
    print(zlib.decompress(zlib.compress(text)))
