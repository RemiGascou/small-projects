# -*- coding: utf-8 -*-

from Stack import Stack

class HTMLParser(object):
    """docstring for HTMLParser."""
    def __init__(self, htmltext):
        def rmsep(s):
            while s.startswith(" ") or  s.startswith("\t") : s=s[1:]
            return s
        super(HTMLParser, self).__init__()
        self.htmltext       = [rmsep(line) for line in htmltext.replace("</", "\n</").replace(">", ">\n").split("\n") if rmsep(line) != "\n" and rmsep(line) !=""]
        self.tags_stack     = Stack()
        self.parsedresult   = []

    def to_be_ignored(self,line):
        if line == "<!DOCTYPE html>": return True
        elif line.startswith("<!--"): return True
        else: return False

    def parse(self, log=False) :
        def extract_tag_args(line):
            def keyword_args(kwargs):
                while kwargs.startswith(" "): kwargs=kwargs[1:]
                keyword = kwargs.split("=\"", 1)[0]
                args = kwargs[kwargs.index("\"")+1:]
                if args.endswith("\""):   args=args[:-1]
                elif args.endswith("\'"): args=args[:-1]
                if " " in args: args = args.split(" ")
                return keyword, args
            if line.startswith("<"): line=line[1:]
            if line.endswith("/>"):  line=line[:-2]
            elif line.endswith(">"): line=line[:-1]
            kwargs = []
            if " " in line:
                tagname = line.split(" ", 1)[0]
                line = line[line.index(" "):]
                for e in line.split("\" ") :
                    kw, args = keyword_args(e)
                    kwargs.append([kw, args])
            else:
                tagname = line
            # Creating attrs dict
            attrs = {}
            for element in kwargs:
                attrs[element[0]] = element[1]
            return (tagname, attrs)
        # ========================================================
        self.parsedresult = []
        for k in range(len(self.htmltext)) :
            line = self.htmltext[k]
            if self.to_be_ignored(line):
                if log: print("[IGNORED]", line)
            elif line.startswith("</") and line.endswith(">"):
                tagname = line[2:-1]
                self.parsedresult.append(self.tags_stack.pop(tagname, k))
                if log: print(self.tags_stack.currentstack())

            elif line.startswith("<") and line.endswith("/>"):
                tagname, attrs = extract_tag_args(line)
                self.tags_stack.push(tagname, k, attrs)
                self.parsedresult.append(self.tags_stack.pop(tagname, k))
                if log: print(self.tags_stack.currentstack())

            elif line.startswith("<") and line.endswith(">"):
                tagname, attrs = extract_tag_args(line)
                self.tags_stack.push(tagname, k, attrs)
                if log: print(self.tags_stack.currentstack())
            # Sort self.parsedresult by value of key linein
            self.parsedresult = sorted(self.parsedresult, key=lambda t: t["linein"])
        return self.parsedresult

    def findall_tags(self, tagname):
        if len(self.parsedresult) == 0:
            self.parse()
        out = []
        for entry in self.parsedresult:
            if entry["name"] == tagname : out.append(self.htmltext[entry["linein"]:entry["lineout"]+1])
        return out

    def autoindent(self): # working fine
        currentindent=0
        out = ""
        for line in self.htmltext :
            if self.to_be_ignored(line):
                out += "\t"*currentindent + line + "\n"
            elif line.startswith("</") and line.endswith(">"):
                currentindent = max(currentindent-1, 0)
                out += "\t"*currentindent + line + "\n"
            elif line.startswith("<!--"):
                out += "\t"*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith("/>"):
                out += "\t"*currentindent + line + "\n"
            elif line.startswith("<") and line.endswith(">"):
                out += "\t"*currentindent + line + "\n"
                currentindent += 1
            else:
                out += "\t"*currentindent + line + "\n"
        return out
