#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from PIL import Image

class UlamSpiral(object):
    """docstring for UlamSpiral."""

    def __init__(self, size, log=True):
        super(UlamSpiral, self).__init__()
        self.log = log
        if size % 2 == 0:
            if self.log : print("[WARN] size "+str(size)+" is even. size will be set to size + 1 = "+str(size+1))
            self.size = size + 1
        else: self.size = size
        self.grid = []
        self.initgrid()

    def initgrid(self):
        """Documentation for initgrid"""
        if self.log : print("[LOG] initgrid()")
        for k in range(self.size):
            self.grid.append(["_"]*self.size)
        return

    def coords(self):
        """Documentation for coords"""
        def addcoordbetween(coords, new):
            betweencoord = []
            diff = (coords[-1][0] - new[0], coords[-1][1] - new[1])
            if diff != (0,0) :
                if   diff[0] != 0:
                    if diff[0] > 0:   # X going LEFT
                        coords += [(coords[-1][0]-k, new[1]) for k in range(0, diff[0])] + [(new[0], new[1])]
                    else:             # X going RIGHT
                        coords += [(coords[-1][0]+k-1, new[1]) for k in range(1, abs(diff[0])+1)] + [(new[0], new[1])]
                elif diff[1] != 0:
                    if diff[1] > 0:   # Y going UP
                        coords += [(new[0], coords[-1][1]-k) for k in range(1, diff[1])]
                    else:             # Y going DOWN
                        coords += [(new[0], coords[-1][1]+k) for k in range(1, abs(diff[1]))]
        #=======================================================================
        # if self.log : print("[LOG] coords()")
        center = (int(self.size / 2), int(self.size / 2))
        coords = [center, (center[0]+1,center[1]+0)]
        for k in range(1, self.size//2+1):
            new_NW = (1*k+center[0],-1*k+center[1])
            addcoordbetween(coords, new_NW)
            new_NE = (-1*k+center[0],-1*k+center[1])
            addcoordbetween(coords, new_NE)
            new_SE = (-1*k+center[0],1*k+center[1])
            addcoordbetween(coords, new_SE)
            new_SW = (1*k+center[0]+1,1*k+center[1])
            addcoordbetween(coords, new_SW)
            new_SW = (1*k+center[0]+1,1*k+center[1])
            addcoordbetween(coords, new_SW)
        return coords[:-1]

    def diag_spiral_coords(self):
        """Documentation for coords"""
        center = (int(self.size / 2), int(self.size / 2))
        coords = [center, center+(1,0)]
        for k in range(self.size//2+1):
            for d in [(1,-1), (-1,-1), (-1, 1), (1,1)]:
                new = (d[0]*k+center[0],d[1]*k+center[1])
                coords.append(new)
            print(coords)
        return coords

    def gendata(self):
        """Documentation for gen"""
        if self.log : print("[LOG] gendata()")
        k = 1
        for c in self.coords():
            if k % ((self.size**2)//10) == 0 and self.log : print("[LOG] Currently at "+str(round(k/(self.size**2)*100, 3))+"%") 
            self.grid[c[1]][c[0]] = int(self.isPrime(k))
            k += 1
        return self.grid

    def isPrime(self, n):
        if n<= 1 :
            return False
        else :
            for k in range(2,int(n**(0.5)+1)):
                if n % k == 0:
                    return False
            return True

    def createimg(self, imgname):
        """Documentation for """
        if self.log : print("[LOG] createimg()")
        if self.log : print("    | grid size  = (%d, %d)" % (len(self.grid[0]), len(self.grid)))
        im = Image.new('RGB', (len(self.grid[0]), len(self.grid)))    # Create the image
        if self.log : print("    | image size = (%d, %d)" % im.size)
        pixels = im.load()                  # Create the pixel map
        for x in range(0, len(self.grid)):         # For every column :
            line = self.grid[x]
            for y in range(0, len(line)):     # For every row
                pixels[y, x] = (line[y]*255, line[y]*255, line[y]*255)
        if self.log : print("    | saving image ...")
        if imgname.split(".")[-1].lower() in [".png",".bmp",".jpg"]:
            im.save(imgname)
        else:
            im.save('.'.join(imgname.split(".")[:-1]+["bmp"]))
        if self.log : print("    | done.")

import sys
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage : python3 "+sys.argv[0]+" SIZE OUTIMAGE")
    else :
        size = int(sys.argv[1])
        outimage = sys.argv[2]
        u = UlamSpiral(size)
        u.gendata()
        u.createimg(outimage)
