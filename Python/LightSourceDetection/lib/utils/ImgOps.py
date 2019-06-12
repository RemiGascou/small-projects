#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

class ImgOps(object):
    """docstring for ImgOps."""

    def __init__(self):
        super(ImgOps, self).__init__()

    def get_near_coords(self, x, y, max_x, max_y, size=1):
        coords = []
        for x_k in [x+k for k in range(-size,size+1)]:
            for y_k in [y+k for k in range(-size,size+1)]:
                if x_k >= 0 and x_k <= max_x and y_k >= 0 and y_k <= max_y:
                    coords.append((x_k, y_k))
        return coords
