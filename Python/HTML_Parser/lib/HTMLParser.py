# -*- coding: utf-8 -*-

from lib.Stack import Stack

class HTMLParser(object):
    """docstring for HTMLParser."""
    def __init__(self, htmltext):
        def rmsep(s):
            while s.startswith(" ") or  s.startswith("\t") : s=s[1:]
            return s
        super(HTMLParser, self).__init__()
        self.htmltext       = [rmsep(line) for line in htmltext.replace("<", "\n<").replace(">", ">\n").split("\n") if rmsep(line) != "\n" and rmsep(line) !=""]
        self.tags_stack     = Stack()
        self.parsedresult   = []

    def to_be_ignored(self,line):
        if line == "<!DOCTYPE html>": return True
        elif line.startswith("<!--"): return True
        else: return False

    def parse(self, log=False) :
        def tagparser(line):
            if line.startswith("<"): line=line[1:]
            if line.endswith("/>"):  line=line[:-2]
            elif line.endswith(">"): line=line[:-1]
            line = line.split(" ", 1)
            tagname = line[0]
            line = line[1]
            tmp = {
                "parsing_args" : False,
                "expected_end" : "",
                "kw_name" : "",
                "kw_args" : [],
                "kw_arg" : ""
            }
            attrs = {}

            lastc = ""
            for c in line:
                #print(c, end=" ")
                if c in ["\"", "\'"] and lastc != "\\":
                    if tmp["parsing_args"] == True:
                        #print("\n[END] args")
                        tmp["kw_args"].append(tmp["kw_arg"])
                        if len(tmp["kw_args"]) == 1 : tmp["kw_args"]=tmp["kw_args"][0]
                        attrs[tmp["kw_name"]] = tmp["kw_args"]
                        tmp["parsing_args"] = False
                        tmp["kw_name"]  = ""
                        tmp["kw_args"]  = []
                        tmp["kw_arg"]   = ""
                    else:
                        #print("\n[BEGIN] args")
                        tmp["parsing_args"] = True
                else:
                    if tmp["parsing_args"]:
                        if c == " ":
                            tmp["kw_args"].append(tmp["kw_arg"])
                            tmp["kw_arg"] = ""
                        else:
                            tmp["kw_arg"] += c
                    else:
                        if c != " " and c != "=": tmp["kw_name"] += c
                lastc = c
            return tagname, attrs
        # ========================================================
        self.parsedresult = []
        for k in range(len(self.htmltext)) :
            line = self.htmltext[k]
            if self.to_be_ignored(line):
                if log: print("[IGNORED]", line)
            elif line.startswith("</") and line.endswith(">"):
                tagname = line[2:-1]
                self.parsedresult.append(self.tags_stack.pop(tagname, k))
                if log: print(self.tags_stack.currentstack(), "\n")

            elif line.startswith("<") and line.endswith("/>"):
                if " " in line:
                    tagname, attrs = tagparser(line)
                else:
                    tagname = line[1:-2]
                self.tags_stack.push(tagname, k, attrs, log)
                self.parsedresult.append(self.tags_stack.pop(tagname, k, log))
                if log: print(self.tags_stack.currentstack(), "\n")

            elif line.startswith("<") and line.endswith(">"):
                if " " in line:
                    tagname, attrs = tagparser(line)
                else:
                    tagname = line[1:-1]
                self.tags_stack.push(tagname, k, attrs, log)
                if log: print(self.tags_stack.currentstack(), "\n")
            # Sort self.parsedresult by value of key linein
            self.parsedresult = sorted(self.parsedresult, key=lambda t: t["linein"])
        return self.parsedresult

    def to_text(self, entry):
        if entry in self.parsedresult:
            return '\n'.join(self.htmltext[entry["linein"]:entry["lineout"]+1])

    def find_by_tag(self, tagname):
        if len(self.parsedresult) == 0:
            self.parse()
        out = []
        for entry in self.parsedresult:
            if entry["name"] == tagname :
                out.append(entry)
                #out.append('\n'.join(self.htmltext[entry["linein"]:entry["lineout"]+1]))
        return out

    def find_by_property(self, prop, value=""):
        if len(self.parsedresult) == 0:
            self.parse()
        out = []
        if value != "":
            for entry in self.parsedresult:
                for key in entry["attrs"].keys():
                    if key == prop :
                        if entry["attrs"][key] == value:
                            out.append(entry)
                            #out.append('\n'.join(self.htmltext[entry["linein"]:entry["lineout"]+1]))
        else:
            for entry in self.parsedresult:
                for key in entry["attrs"].keys():
                    if key == prop :
                        out.append(entry)
                        #out.append('\n'.join(self.htmltext[entry["linein"]:entry["lineout"]+1]))
        return out

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
