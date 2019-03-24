# -*- coding: utf-8 -*-
import os, sys
from lib import *


class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def push(self, name, linein, attrs={}, log=False):
        data = {
            "name"      : name,
            "linein"    : linein,
            "lineout"   : -1,
            "attrs"     : attrs
        }
        self.stack.append(data)
        if log: print("[PUSH]", self.stack[-1])

    def pop(self, name, lineout, log=False):
        if len(self.stack) != 0:
            if self.stack[-1]["name"] != name:
                print("[WARN] First element of the stack is \"" + self.stack[-1]["name"] +"\" and not \"" + name + "\"")
                return None
            else:
                data = self.stack[-1]
                data["lineout"] = lineout
                self.stack = self.stack[:-1]
                if log: print("[POP_]", data)
                return data
        else:
            return None

    def currentstack(self):
        stack_el_names = [e["name"] for e in self.stack]
        if len(stack_el_names) != 0:
            maxlen = max([len(e) for e in stack_el_names])
            return '\n'.join(["|" + name.center(maxlen, " ") + "|" for name in stack_el_names[::-1]]) + "\n|" + "_"*maxlen + "|"
        else:
            return "\n|_EMPTY_STACK_|"

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


if __name__ == '__main__':
    url = """https://www.root-me.org/"""

    os.system("wget " + url + sys.argv[1] + " -o out.html")

    f = open("out.html", "r")
    html = '\n'.join(f.readlines())
    f.close()



    hp = HTMLParser(html)
    hp.parse(log=False)

    data_pseudo = hp.to_text(hp.find_by_property("itemprop", value="givenName")[0])
    hp2 = HTMLParser(data_pseudo)
    hp2.parse(log=False)
    d = hp2.find_by_tag("img")[0]
    pseudo = d["attrs"]["alt"]
    logo_link = d["attrs"]["src"]
    print("pseudo    :", pseudo)
    print("logo_link :", url+logo_link)
    data_score = [e for e in hp.find_by_tag("span") if e["attrs"]["class"] == ['color1', 'tl']][:2]
    score = hp.to_text(data_score[0]).replace("\n", "").split("&nbsp;")[0].split("<span class=\"color1 tl\">")[1]
    print("score     :", score)
    rank = hp.to_text(data_score[1]).replace("\n", "").replace("<span class=\"gris\">", "").replace("<span class=\"color1 tl\">", "").replace("</span></span>", "").split("/")
    print("rank      :", rank)
