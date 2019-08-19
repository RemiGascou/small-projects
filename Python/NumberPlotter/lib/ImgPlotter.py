#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

import math
from PIL import Image

from .ColorMap import *

class ImgPlotter(object):
    """docstring for ImgPlotter."""

    def __init__(self, log=True, size=(0,0)):
        self.log = log
        if self.log : print("[LOG] __init__()")
        super(ImgPlotter, self).__init__()
        self.size       = size
        self.data       = []
        self.colormap   = {
            "0" : (200,200,200), # gray
            "1" : (0,0,0),       # black
            "2" : (255,255,0),   # yellow
            "3" : (0,255,0),     # green
            "4" : (128,64,0),    # brown
            "5" : (255,0,0),     # red
            "6" : (255,0,255),   # violet
            "7" : (0,0,0),       #
            "8" : (0,0,0),       #
            "9" : (255,255,255)  # white
        }

    def gendata(self, nmax, modifier=lambda x : x):
        """Documentation for gendata"""
        if self.log : print("[LOG] gendata()")
        self.data, k, buffer = [], 0, ""
        while k < nmax:
            buffer += str(modifier(k))
            if len(buffer) >= 80:
                self.data.append(buffer)
                buffer = ""
            k += 1
        if len(buffer) != 0: self.data.append(buffer)
        if   self.size == (0,0) : self.squaresize()
        elif self.size[1] == 0  : self.autosize()
        txtdata = ''.join(self.data)
        temp    = [txtdata[k*self.size[0]:(k+1)*self.size[0]] for k in range(len(txtdata)//self.size[0])]
        temp   += [txtdata[len(txtdata)-len(txtdata)%self.size[0]:].ljust(self.size[0],'0')]
        self.data = temp
        return self.data

    def squaresize(self):
        """Documentation for squaresize"""
        if self.log : print("[LOG] squaresize()")
        total       = len("".join(self.data))
        size        = math.ceil(math.sqrt(total))
        self.size   = (size, size)
        if self.log : print("    | self.size = (%d, %d)" % self.size)
        return self

    def autosize(self):
        """Documentation for squaresize"""
        if self.log : print("[LOG] autosize()")
        total       = len("".join(self.data))
        height      = math.ceil(total / self.size[0])
        self.size   = (self.size[0], height)
        if self.log : print("    | self.size = (%d, %d)" % self.size)
        return self

    def savedata(self, filename):
        """Documentation for savedata"""
        if self.log : print("[LOG] savedata()")
        f = open(filename, "w")
        for e in self.data:
            f.write(e)
        f.close()
        return self

    def createimg(self, imgname):
        """Documentation for """
        if self.log : print("[LOG] createimg()")
        if self.log : print("    | data size  = (%d, %d)" % (len(self.data[0]), len(self.data)))
        im = Image.new('RGB', (len(self.data[0]), len(self.data)))    # Create the image
        if self.log : print("    | image size = (%d, %d)" % im.size)
        pixels = im.load()                  # Create the pixel map
        for x in range(0, len(self.data)):         # For every column :
            line = self.data[x]
            for y in range(0, len(line)):     # For every row
                pixels[y, x] = self.colormap[line[y]]
        if self.log : print("    | saving image ...")
        im.save(imgname)
        if self.log : print("    | done.")

    def get_colormap (self):
        return self.colormap

    def set_colormap (self, colormap):
        self.colormap = colormap
        return self
