#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

class ColorMap(object):
    """docstring for ColorMap."""

    def __init__(self):
        super(ColorMap, self).__init__()
        self.colormap   = {}
        self.set_syn()

    def set_syn(self):
        """Documentation for set_syn"""
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
        return self

    def set_9grayscale(self):
        """Documentation for set_syn"""
        self.colormap   = {str(key) : (int((255/9)*key),int((255/9)*key),int((255/9)*key)) for key in list(range(10))}
        return self

    def current(self):
        """Documentation for current"""
        return self.colormap
