#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import random
import argparse
import os,sys

def readfile(file, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "r"+b_opt)
    data = f.readlines()
    f.close()
    return data

def writefile(file, data, binary=False):
    if binary : b_opt="b"
    else:       b_opt=""
    f = open(file, "w"+b_opt)
    f.write(data)
    f.close()
    return data

def accentuate_decode(data:bytes, inverted=False):
    """Documentation for accentuate_decode"""
    table_normal   = { '0' : list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]_{|}~'), '1' : list("âêîôûŷéèàù")}
    table_inverted = { '0' : table_normal['1'], '1' : table_normal['0'] }
    if inverted == True:
        out_data = ''
        for c in data:
            if c in table_inverted['0']   : out_data += '0'
            elif c in table_inverted['1'] : out_data += '1'
    else :
        out_data = ''
        for c in data:
            if c in table_normal['0']   : out_data += '0'
            elif c in table_normal['1'] : out_data += '1'
    bindata = bytes([int(out_data[8*k:8*(k+1)],2) for k in range(0, len(data)//8)])
    return bindata

def accentuate_encode(data:bytes, inverted=False):
    """Documentation for accentuate_encode"""
    table_normal   = { '0' : list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]_{|}~'), '1' : list("âêîôûŷéèàù")}
    table_inverted = { '0' : table_normal['1'], '1' : table_normal['0'] }
    bindata = ''.join([bin(c)[2:].rjust(8,'0') for c in data])
    if inverted == True:
        out_data = ''.join([random.choice(table_inverted[bit]) for bit in bindata])
    else :
        out_data = ''.join([random.choice(table_normal[bit]) for bit in bindata])
    return out_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",  required="True", help="Input file", type=str)
    parser.add_argument("-q", "--quiet", help="Quiet mode", default=False, action="store_true")
    parser.add_argument("-o", "--output", help="Output file", type=str)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("-e", "--encode", help="Encodes input file", default=False, action="store_true")
    mode.add_argument("-d", "--decode", help="Decodes input file", default=False, action="store_true")
    parser.add_argument("-i", "--invert", help="Output file", type=str)
    args = parser.parse_args()

    if not args.quiet : print("==============[ Accentuate Encoder ]==============")
    if args.encode == True:
        if not args.quiet : print("\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Encoding Mode.")
        if not os.path.exists(args.file) :
            if not args.quiet : print("\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m File %s does not exist." % args.file)
            sys.exit(-1)
        if args.output == None : args.output = args.file + '.encoded'
        indata  = b'\n'.join(readfile(args.file, binary=True))
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Read %d bytes." % len(indata))
        outdata = accentuate_encode(indata)
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Writting %d bytes to file %s ..." % (len(outdata), args.output))
        writefile(args.output, outdata)
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Done !")
    else:
        if not args.quiet : print("\x1b[1m[\x1b[93mLOG\x1b[0m\x1b[1m]\x1b[0m Decoding Mode.")
        if not os.path.exists(args.file) :
            if not args.quiet : print("\x1b[1m[\x1b[91mWARN\x1b[0m\x1b[1m]\x1b[0m File %s does not exist." % args.file)
            sys.exit(-1)
        if args.output == None : args.output = args.file.replace(".encoded","") + '.decoded'
        indata  = '\n'.join(readfile(args.file))
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Read %d bytes." % len(indata))
        outdata = accentuate_decode(indata)
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Writting %d bytes to file %s ..." % (len(outdata), args.output))
        writefile(args.output, outdata, binary=True)
        if not args.quiet : print("\x1b[1m[\x1b[93m+\x1b[0m\x1b[1m]\x1b[0m Done !")
