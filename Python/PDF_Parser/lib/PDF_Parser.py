# -*- coding: utf-8 -*-

class PDF_Parser(object):
    """docstring for PDF_Parser."""
    def __init__(self, filename):
        super(PDF_Parser, self).__init__()
        self.filename = filename
        f = open(filename, 'rb')
        self.rawdata = f.readlines()
        f.close()
        self.parse()

    def parse(self, log = False):
        """Documentation for parse"""
        def ignore(line, parsing_state):
            if line.startswith(b"%") and parsing_state["in_obj"]==False and parsing_state["in_stream"]==False : return True
            else: return False
        parsing_state = {"in_obj" : False, "in_stream" : False}
        #=========================================
        obj = {}
        for k in range(len(self.rawdata)):
            line = self.rawdata[k]
            if not ignore(line, parsing_state):
                if line.endswith(b"endobj\n"):
                    if log : print("[<OBJ] endobj")
                    obj["location"]["line_end"] = k
                    print(obj)
                    if log : print()
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
