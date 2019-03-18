# -*- coding: utf-8 -*-


class Phrack2Latex(object):
    """docstring for Phrack2Latex."""

    def __init__(self):
        super(Phrack2Latex, self).__init__()
        self.texcmd     = TexCMD()
        self.dataout    = []

    def parse(self, filename):
        """Documentation for parse"""
        f = open(filename, "r")
        data = f.readlines()
        f.close()
        for line in data:
            if "Volume" in line.split(" ") and "Issue" in line.split(" "):
                l = line.split(" ")
            elif line.startswith("--[ ") and not line.startswith("--[ Contents"):
                self.dataout.append(self.texcmd.section(' '.join(line.split(" ")[3:]))
            else:
                self.dataout.append(self.texcmd.comment(line))
        return self.dataout
