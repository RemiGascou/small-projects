# -*- coding: utf-8 -*-

import zlib

class PDF_Parser(object):
    """docstring for PDF_Parser."""
    def __init__(self, filename, log=False):
        super(PDF_Parser, self).__init__()
        self.filename = filename
        self._log = log
        self.rawdata = self.__loadPDF(self.filename)
        self.parsed_result = {
            "objects" : [],
            "xref" : []
        }
        self.parse()

    def __loadPDF(self, filename):
        """Documentation for __loadPDF"""
        f = open(filename, 'rb')
        rawdata = f.readlines()
        f.close()
        return rawdata

    def find_obj_by_ref(self, obj_ref, log=False):
        """ Documentation for find_obj_by_ref
            int obj_ref : object reference
        """
        log = self._log or log
        if log : print("[FIND] obj ref="+str(obj_ref))
        out = []
        for obj in self.parsed_result["objects"]:
            if obj["obj_data"]["ref"] == obj_ref:
                out.append(obj)
                #out.append(self.rawdata[obj["location"]["line_begin"]:obj["location"]["line_end"]])
        if len(out) == 1:
            out = out[0]
        return out

    def parse(self, log=False):
        """Documentation for parse"""
        #========================================
        def objs_parse(line_begin, line_end):
            def ignore(line, parsing_state):
                if line.startswith(b"%") and parsing_state["in_obj"]==False and parsing_state["in_stream"]==False : return True
                else: return False
            obj = {}
            parsing_state = {"in_obj" : False, "in_stream" : False}
            for k in range(len(self.rawdata[line_begin:line_end])):
                line = self.rawdata[k]
                if not ignore(line, parsing_state):
                    if line.endswith(b"endobj\n"):
                        parsing_state["in_obj"]=False
                        if log : print("[<OBJ] endobj\n",obj,"\n")
                        obj["location"]["line_end"] = k
                        self.parsed_result["objects"].append(obj)
                    elif line.endswith(b"obj\n"):
                        parsing_state["in_obj"]=True
                        line = line.split(b" ")
                        if log : print("[>OBJ] obj, ref="+str(line[0])+" gen_num="+str(line[1]))
                        obj = { "location" : {"line_begin":k,"line_end":-1},
                                "obj_data" : {"ref" : int(line[0]),"gen_num" : int(line[1]),"data" : [], "stream" : []}
                        }
                    elif parsing_state["in_obj"]==True:
                        if line.endswith(b"endstream\n"):
                            if log : print("[OBJ::<stream] endstream\n",obj,"\n")
                            parsing_state["in_stream"] = False
                        elif line.endswith(b"stream\n"):
                            parsing_state["in_stream"] = True
                        elif parsing_state["in_stream"]==False:
                            obj["obj_data"]["data"].append(line)
                        elif parsing_state["in_stream"]==True:
                            obj["obj_data"]["stream"].append(line)

        #=========================================
        log = self._log or log
        sections = self.detect_sections()
        objs_parse(sections["objs"]["begin"], sections["objs"]["end"])
        return self.parsed_result["objects"]

    def detect_sections(self, log=False):
        sections = {
            "header"  : {"_in":False,"begin":0,"end":0},
            "objs"    : {"_in":False,"begin":0,"end":0},
            "xref"    : {"_in":False,"begin":0,"end":0},
            "trailer" : {"_in":False,"begin":0,"end":0}
        }
        sections["header"]["begin"] = 0;
        sections["header"]["_in"]   = True;
        for k in range(len(self.rawdata)):
            line = self.rawdata[k]
            if line.endswith(b"obj\n") and sections["header"]["_in"] == True:
                sections["header"]["end"] = k-1;
                sections["header"]["_in"] = False;
                sections["objs"]["begin"] = k;
                sections["objs"]["_in"]   = True;
            elif line.endswith(b"xref\n") and sections["objs"]["_in"] == True:
                sections["objs"]["end"] = k-1;
                sections["objs"]["_in"]   = False;
                sections["xref"]["begin"] = k;
                sections["xref"]["_in"] = True;
            elif line.endswith(b"trailer\n") and sections["xref"]["_in"] == True:
                sections["xref"]["end"]   = k-1;
                sections["xref"]["_in"]   = False;
                sections["trailer"]["begin"] = k;
                sections["trailer"]["_in"]   = True;
        if sections["trailer"]["_in"] == True and sections["trailer"]["end"] == 0:
            sections["trailer"]["end"] = k;
        for key in sections.keys():
            del sections[key]["_in"]
        return sections

if __name__ == '__main__':
    PDF_Parser("out.pdf")
