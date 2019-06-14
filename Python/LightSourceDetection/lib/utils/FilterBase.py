#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : FilterBase
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

class FilterBase(object):
    """docstring for FilterBase."""

    def __init__(self, imagefile, size=1, filter_callback=lambda n,p : (0,0,0)):
        super(FilterBase, self).__init__()
        # Found pixels will be send as a list to
        # self._pil_image = __import__("PIL")

        self._numpy     = __import__("numpy")
        self.imagefile  = imagefile
        self.outimg     = None
        self.filter_callback = filter_callback

    def run(self):
        """Documentation for run"""
        def get_near_coords(x, y, max_x, max_y, size=1):
            coords = []
            for x_k in [x+k for k in range(-size,size+1)]:
                for y_k in [y+k for k in range(-size,size+1)]:
                    if x_k >= 0 and x_k <= max_x and y_k >= 0 and y_k <= max_y:
                        coords.append((x_k, y_k))
            return coords
        # Processing
        from PIL import Image
        im              = Image.open(self.imagefile)
        width, height   = im.size
        npix            = self._numpy.array(im)
        matrix          = self._numpy.zeros((npix.shape[0], npix.shape[1], 3), dtype=self._numpy.uint8)
        pixels = im.load()

        for y in range(npix.shape[1]):
            for x in range(npix.shape[0]):
                neighbors = get_near_coords(x, y, width-1, height-1)
                # Calcul
                (r, g, b) = self.filter_callback(neighbors,pixels)
                try:
                    matrix[y][x] = (r, g, b)
                except :
                    pass
        if type(matrix) != None:
            self.outimg = Image.fromarray(matrix, 'RGB')
        return self.outimg


if __name__ == '__main__':
    def filter_callback(neighbors, pixels):
        """Documentation for filter_callback
            Takes two arguments :
            - neighbors : list of coords (x, y) of neighbors pixels in radius 'size'
            - pixels : pixelmap of the image
        """
        # Begin Body ==============================
        maxi = (255)**9
        r_value, g_value, b_value = 1, 1, 1
        for ne in neighbors:
            (r, g, b) = pixels[ne[0], ne[1]]
            r_value += r
            g_value += g
            b_value += b
        r, g, b = int(r_value/(len(neighbors)+1)), int(g_value/(len(neighbors)+1)), int(b_value/(len(neighbors)+1))
        # r, g, b = int(((r_value)/maxi) * 255), int(((g_value)/maxi) * 255), int(((b_value)/maxi) * 255)
        # End Body ================================
        return (r, g, b)

    f = FilterBase("../../o.jpg", filter_callback).run().save("outtrest.bmp")
