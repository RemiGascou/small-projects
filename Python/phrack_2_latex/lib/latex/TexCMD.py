# -*- coding: utf-8 -*-


class TexCMD(object):
    """docstring for TexCMD."""

    def __init__(self, arg):
        super(TexCMD, self).__init__()
        self.arg = arg

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
