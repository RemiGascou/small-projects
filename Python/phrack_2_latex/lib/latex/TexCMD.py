# -*- coding: utf-8 -*-


class TexCMD(object):
    """docstring for TexCMD."""

    def __init__(self):
        super(TexCMD, self).__init__()

    def comment(self, s):
        return "%" + s

    def section(self, s):
        return "\\section{"+s+"}"

    def subsection(self, s):
        return "\\subsection{"+s+"}"

    def subsubsection(self, s):
        return "\\subsubsection{"+s+"}"

    def comment(self, s):
        return "%" + s

    def tableofcontents(self):
        return "\\tableofcontents{}"

    def title(self, s):
        return "\\title{"+s+"}"

    def author(self, s):
        return "\\author{"+s+"}"

    def date(self, s):
        return "\\date{"+s+"}"
