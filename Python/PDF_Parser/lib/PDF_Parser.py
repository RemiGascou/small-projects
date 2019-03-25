# -*- coding: utf-8 -*-

class PDF_Parser(object):
    """docstring for PDF_Parser."""
    def __init__(self, filename, log=False):
        super(PDF_Parser, self).__init__()
        self.filename = filename
        self._log = log
        self.rawdata = self.__loadPDF(self.filename)
        self.parsed_result = {
            "objects" : []
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
                out.append(self.rawdata[obj["location"]["line_begin"]:obj["location"]["line_end"]])
        return out



    def parse(self, log=False):
        """Documentation for parse"""
        def ignore(line, parsing_state):
            if line.startswith(b"%") and parsing_state["in_obj"]==False and parsing_state["in_stream"]==False : return True
            else: return False
        log = self._log or log
        parsing_state = {"in_obj" : False, "in_stream" : False}
        #=========================================
        obj = {}
        for k in range(len(self.rawdata)):
            line = self.rawdata[k]
            if not ignore(line, parsing_state):
                if line.endswith(b"endobj\n"):
                    if log : print("[<OBJ] endobj")
                    obj["location"]["line_end"] = k
                    if log : print(obj,"\n")
                    self.parsed_result["objects"].append(obj)
                elif line.endswith(b"obj\n"):
                    line = line.split(b" ")
                    if log : print("[>OBJ] obj, ref="+str(line[0])+" gen_num="+str(line[1]))
                    obj = {
                        "location" : {"line_begin":k,"line_end":-1},
                        "obj_data" : {
                            "ref" : int(line[0]),
                            "gen_num" : int(line[1]),
                            "rawdata" : []
                        }
                    }
        return None

if __name__ == '__main__':
    PDF_Parser("out.pdf")
