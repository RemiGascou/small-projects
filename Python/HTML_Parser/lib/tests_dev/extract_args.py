
tests = """
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Esoteric_programming_language rootpage-Esoteric_programming_language skin-vector action-view" action="POST" wtfarg="TEST">
<div class='testsclass'>
<div class='testsclass' style="teststyle">
<div class='' style="space after" >
<nav class="top-bar" data-topbar>
"""

b = """<div class="testsclass">"""

def extract_tag_args(line):
    def keyword_args(kwargs):
        #print(kwargs, len(kwargs))
        while kwargs.startswith(" "): kwargs=kwargs[1:]
        if "=\"" in kwargs:
            keyword = kwargs.split("=\"", 1)[0]
            args = kwargs[kwargs.index("\"")+1:]
        elif "=\'" in kwargs:
            keyword = kwargs.split("=\'", 1)[0]
            args = kwargs[kwargs.index("\'")+1:]
        if args.endswith("\""):   args=args[:-1]
        elif args.endswith("\'"): args=args[:-1]
        if " " in args: args = args.split(" ")
        return keyword, args
    if line.startswith("<"): line=line[1:]
    if line.endswith("/>"):  line=line[:-2]
    elif line.endswith(">"): line=line[:-1]
    kwargs = []
    print(line)
    if " " in line:
        tagname = line.split(" ", 1)[0]
        line = line[line.index(" "):]

        if "\" " in line and "\' " in line:
            print("next =>", min([line.index("\" "), line.index("\' ")]))

        for e in line.split("\" ") :  # And \" ??
            if e != "":
                kw, args = keyword_args(e)
                kwargs.append([kw, args])
    else:
        tagname = line
    # Creating attrs dict
    attrs = {}
    for element in kwargs:
        attrs[element[0]] = element[1]
    return (tagname, attrs)


for line in tests.split("\n") :
    if line != "":
        print(line)
        tagname, attrs = extract_tag_args(line)
        print(tagname+":")
        for key in attrs.keys():
             print("\t",key,":",attrs[key])
        input()
