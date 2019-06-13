
def tagparser(line):
    if line.startswith("<"): line=line[1:]
    if line.endswith("/>"):  line=line[:-2]
    elif line.endswith(">"): line=line[:-1]
    line = line.split(" ", 1)
    tagname = line[0]
    line = line[1]
    tmp = {"parsing_args" : False,"expected_end" : "","kw_name" : "","kw_args" : [],"kw_arg" : ""}
    attrs = {}

    lastc = ""
    for c in line:
        #print(c, end=" ")
        if c in ["\"", "\'"] : #and lastc != "\\":
            if tmp["parsing_args"] == True:
                #print("\n[END] args")
                tmp["kw_args"].append(tmp["kw_arg"])
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
        # lastc = c
    return tagname, attrs

if __name__ == '__main__':
    tests = [
        """<link rel="alternate" type="application/rss+xml" title="RSS [Root Me : plateforme d&#039;apprentissage d&#233;di&#233;e au Hacking et &#224; la S&#233;curit&#233; de l&#039;Information]" href="https://www.root-me.org?page=backend&amp;lang=fr" />""",
        """nav class="top-bar" style='navbar top black'""",
        """<div class='testsclass'>""",
        """<div class='testsclass' style="teststyle">""",
        """<div class='' style="space after" >""",
        """<nav class="top-bar" data-topbar>"""
    ]

    for test in tests:
        print("\x1b[1m[TEST]",test,"\x1b[0m")
        tagname, attrs = tagparser(test)
        print(tagname, ":")
        for key in attrs.keys():
            print("| ",key, ":", attrs[key])
        print()
