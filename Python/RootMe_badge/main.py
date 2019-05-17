from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Badge(object):
    """docstring for Badge."""
    def __init__(self, pseudo, points, rank, maxrank, badge):
        super(Badge, self).__init__()
        self.pseudo = pseudo
        self.points = points
        self.rank = rank
        self.maxrank = maxrank
        self.badge = badge

    def export(self, outfile):
        pseudo = "Podalirius"
        points = 725
        rank, maxrank = 7847, 125476
        badge = "newbie"

        img         = Image.new("RGB", (300,100), color=(255,255,255))
        authorlogo  = self.border(Image.open("logo.jpg"), bordersize=1)
        rootmelogo  = self.png_background(Image.open("rootmeskull.png"))
        draw        = ImageDraw.Draw(img)
        fontcolor   = (0,0,0)

        img = self.merge(img, authorlogo, xcoord=10, ycoord=10)
        img = self.merge(img, rootmelogo, xcoord=img.size[0]-rootmelogo.size[0]-10, ycoord=img.size[1]-rootmelogo.size[1]-10)

        fontcolor   = (0,0,0)
        font = ImageFont.truetype("src/BebasNeue-Regular.ttf", 30)
        draw.text((10+authorlogo.size[0]+10,10), self.pseudo[:18], fontcolor,font=font)

        fontcolor   = (100,100,100)
        font = ImageFont.truetype("src/BebasNeue-Regular.ttf", 20)
        draw.text((10+authorlogo.size[0]+10,10+9*authorlogo.size[1]//16), str(self.points) + " Points", fontcolor,font=font)
        img = self.border(img, bordersize=2)
        img.save(outfile)


    def border(self, img, bordersize=1, bordercolor=(0,0,0)):
        pixels = img.load()
        for i in list(range(0, bordersize))+list(range(img.size[0]-bordersize, img.size[0])):         # for every col:
            for j in range(img.size[1]):
                pixels[i,j] = bordercolor
        for i in range(img.size[0]):
            for j in list(range(0, bordersize))+list(range(img.size[1]-bordersize, img.size[1])):     # For every row
                pixels[i,j] = bordercolor
        return img

    def merge(self, img1, img2, xcoord=0,  ycoord=0):
        """Documentation for merge"""
        pixels1 = img1.load()                 # create the pixel map
        pixels2 = img2.load()                 # create the pixel map
        for i in range(img1.size[0]):         # for every col:
            for j in range(img1.size[1]):     # For every row
                (r1, g1, b1) = pixels1[i,j]
                try:
                    pixels1[xcoord+i,ycoord+j] = pixels2[i,j]
                except Exception:
                    pixels1[i,j] = (r1, g1, b1)
        return img1

    def png_background(self, img, backgroundcolor=(255,255,255), alphalevel=0.5):
        """Documentation for merge"""
        pixels = img.load()
        imgout = Image.new("RGB",img.size)
        pixelsout = imgout.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                (r, g, b, a) = pixels[i,j]
                if a <= alphalevel:
                    pixelsout[i,j] = (backgroundcolor[0], backgroundcolor[1], backgroundcolor[2])
                else:
                    pixelsout[i,j] = (int(r*(a/255)), int(g*(a/255)), int(b*(a/255)))
        return imgout

if __name__ == '__main__':
    Badge("Podalirius", 725, 4626, 125541, "newbie").export("badge.bmp")
