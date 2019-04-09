# -*- coding: utf-8 -*-

import sys

from lib.latex import *

class Phrack2Latex(object):
    """docstring for Phrack2Latex."""

    def __init__(self):
        super(Phrack2Latex, self).__init__()
        self.texcmd     = TexCMD()
        self.texdata    = []
        self.data       = {"author":"", "title":""}

    def rmsep(self, line):
        while line.startswith("\t") or line.startswith(" "):
            line = line[1:]
        return line

    def parse(self, filename):
        """Documentation for parse"""
        f = open(filename, "r")
        data = f.readlines()
        f.close()
        for line in data:
            line = self.rmsep(line)
            if "Volume" in line and "Issue" in line:
                l = line.split(" ")
            elif line.startswith("|=-") and line != "|=-----------------------------------------------------------------------=|\n":
                if self.data["title"] == "" :
                    title = ''.join(line.split("[",1)[1].split("]")[:-1])
                    print("title  :",title)
                    self.data["title"] = title
                    self.texdata.append(self.texcmd.title(title))
                elif self.data["author"] == "":
                    author = ''.join(line.split("[",1)[1].split("]")[:-1])
                    print("author :", author)
                    self.data["author"] = author
                    self.texdata.append(self.texcmd.author(author))
            elif line.startswith("--[ ") and not line.startswith("--[ Contents"):
                self.texdata.append(self.texcmd.section(' '.join(line.split(" ")[3:])))
            elif line.startswith("--[ Contents"):
                self.texdata.append(self.texcmd.tableofcontents())
            else:
                self.texdata.append(self.texcmd.comment(line))
        return self.texdata
    def export(self, filename):
        """Documentation for export"""
        try:
            f = open(filename, "w")
            for line in texdata:
                f.write(line)
            f.close()
        except Exception as e:
            return -1
        return 0

if __name__ == '__main__':
    main()
