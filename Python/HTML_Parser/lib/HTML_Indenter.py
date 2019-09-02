#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

class HTML_Indenter(object):
    """docstring for HTML_Indenter."""
    def __init__(self, htmltext):
        def rmsep(s):
            while s.startswith(" ") or  s.startswith("\t") : s=s[1:]
            return s
        super(HTML_Indenter, self).__init__()
        self.htmltext = [rmsep(line) for line in htmltext.replace("<", "\n<").replace(">", ">\n").split("\n") if rmsep(line) != "\n" and rmsep(line) !=""]


    def to_be_ignored(self,line):
        if line == "<!DOCTYPE html>": return True
        elif line.startswith("<!--"): return True
        else: return False

    def autoindent(self, indent="\t"): # working fine
        currentindent=0
        out = ""
        for line in self.htmltext :
            if self.to_be_ignored(line):
                out += indent*currentindent + line + "\n"
            elif line.startswith("</") and line.endswith(">"):
                currentindent = max(currentindent-1, 0)
                out += indent*currentindent + line + "\n"
            elif line.startswith("<!--"):
                out += indent*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith("/>"):
                out += indent*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith(">"):
                out += indent*currentindent + line + "\n"
                currentindent += 1
            else:
                out += indent*currentindent + line + "\n"
        return out

    def autoindent_colored(self, indent="    "):
        def linecolors(line):
            """Documentation for linecolors"""
            if "<!" in line :
                return line
            elif "<" in line :
                line = line.split(" ")
                for k in range(len(line)) :
                    e = line[k]
                    if e.startswith("</")  :
                        if e.endswith(">") :
                            line[k] = "</"+"\x1b[1;91m"+e[2:e.index('>')]+"\x1b[0m"+">"
                        else:
                            line[k] = "<"+"\x1b[1;91m"+e[1:]+"\x1b[0m"
                    elif e.startswith("<") :
                        if e.endswith(">") :
                            line[k] = "<"+"\x1b[1;91m"+e[1:e.index('>')]+"\x1b[0m"+">"
                        else:
                            line[k] = "<"+"\x1b[1;91m"+e[1:]+"\x1b[0m"
                    elif "=" in e :
                        if e.endswith(">") :
                            line[k] = "\x1b[1;93m"+e[:e.index('>')]+"\x1b[0m"+">"
                        else:
                            line[k] = "\x1b[1;93m"+e+"\x1b[0m"
                return ' '.join(line)
            else:
                return line
        currentindent=0
        out = ""
        for line in self.htmltext :
            line = linecolors(line)
            if self.to_be_ignored(line):
                out += indent*currentindent + line + "\n"
            elif line.startswith("</") and line.endswith(">"):
                currentindent = max(currentindent-1, 0)
                out += indent*currentindent + line + "\n"
            elif line.startswith("<!--"):
                out += indent*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith("/>"):
                out += indent*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith(">"):
                out += indent*currentindent + line + "\n"
                currentindent += 1
            else:
                out += indent*currentindent + line + "\n"
        return out
