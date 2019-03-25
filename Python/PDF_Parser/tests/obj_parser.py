# -*- coding: utf-8 -*-

def parse_obj(obj):
    """Documentation for new_function"""
    obj_data = {
        "ref": -1,
        "gen_num" : -1,
        "data" : []
    }

    parse_state = {"in_obj" : False, "in_stream" : False}

    for line in obj:
        if line.endswith(b"obj\n") and len(line.split(b" ")) == 3:
            line = line.split(b" ")
            obj_data["ref"]     = int(line[0])
            obj_data["gen_num"] = int(line[1])
            parse_state["in_obj"] = True
        elif line.endswith(b"endobj\n"):
            parse_state["in_obj"] = False
        else:
            if parse_state["in_obj"]:
                if line not in [b"endstream\n", b"stream\n"]:
                    if parse_state["in_stream"]:
                        obj_data["stream"].append(line)
                    else:
                        obj_data["data"].append(line)

                if line == b"endstream\n":
                    parse_state["in_stream"] = False
                elif line == b"stream\n":
                    parse_state["in_stream"] = True
                    obj_data["stream"] = []

            pass
    return obj_data

f = open("test.pdfobj", "rb")
exobj = f.readlines()
f.close()

if __name__ == '__main__':
    d = parse_obj(exobj)
    for key in d.keys():
        print(key, ":", d[key])
