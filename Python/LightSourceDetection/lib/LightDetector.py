#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from .utils.ImgOps import *

from PIL import Image
import numpy

class LightDetector(object):
    """docstring for LightDetector."""

    def __init__(self, imagefile):
        super(LightDetector, self).__init__()
        self.imagefile  = imagefile
        self.matrix     = None
        self.highest    = 0

    def find_lightsources(self):
        """ Documentation for find_lightsources """
        def vscaled(nei, pixels):
            """Documentation for scaled"""
            maxi = (255*3)**9
            #print("maxi :", maxi)
            value = 1
            for ne in nei:
                p = pixels[ne[0], ne[1]]
                #print("  -> ",p, value)
                value *= p[0] + p[1] + p[2]
            return int(((maxi-value)/maxi) * 255)
        im              = Image.open(self.imagefile)
        width, height   = im.size
        npix            = numpy.array(im)
        matrix          = numpy.zeros((npix.shape[0], npix.shape[1], 3), dtype=numpy.uint8)
        pixels = im.load()

        i = ImgOps()
        for y in range(npix.shape[1]):
            for x in range(npix.shape[0]):
                #print(str(x).rjust(4)," ", str(y).rjust(4),sep="")
                voisins = i.get_near_coords(x, y, width-1, height-1)
                # Calcul
                v = vscaled(voisins,pixels)
                # Update du max connu
                if v > self.highest: self.highest = v
                try:
                    matrix[y][x] = v, v, v
                except :
                    pass
        self.matrix = matrix
        return self

    def export(self):
        """Documentation for export"""
        if type(self.matrix) != None:
            img = Image.fromarray(self.matrix, 'RGB')
            img.save('out.bmp')
            # for y in range(self.matrix.shape[1]-1):
            #     for x in range(self.matrix.shape[0]-1):
            #         print("\r",str(x).rjust(4)," ", str(y).rjust(4), end="",sep="")
            #         voisins = i.get_near_coords(x, y, width-1, height-1)
            #         matrix[x][y]
        return None
