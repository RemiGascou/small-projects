# -*- coding: utf-8 -*-

import zlib

class PDFObject(object):
    """docstring for PDFObject."""
    def __init__(self):
        super(PDFObject, self).__init__()
        self.obj = {
            "location" : {
                "line_begin": k,
                "line_end": -1
            },
            "obj_data" : {
                "ref"     : -1,
                "gen_num" : -1,
                "data"    : [],
                "stream"  : []
            }
        }

    def stream_to_text(self):
        """Documentation for stream_to_text"""
        return zlib.decompress(self.obj["obj_data"]["stream"])

    def text_to_stream(self):
        """Documentation for stream_to_text"""
        self.obj["obj_data"]["stream"] = zlib.compress(text)

    def get_linedelimiters(arg):
        """Documentation for get_linedelimiters"""
        return (self.obj["location"]["line_begin"],self.obj["location"]["line_end"])



if __name__ == '__main__':
    main()
