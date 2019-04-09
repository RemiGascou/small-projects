# -*- coding: utf-8 -*-

from lib import *

if __name__ == '__main__':

    phrackfile = sys.argv[1]
    texfileout = sys.argv[2]
    p = Phrack2Latex()
    p.parse(phrackfile)
    print("[LOG] Exporting to "+texfileout)
    p.export(texfileout)
