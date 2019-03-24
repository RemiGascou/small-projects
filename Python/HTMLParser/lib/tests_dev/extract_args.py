
a = """<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Esoteric_programming_language rootpage-Esoteric_programming_language skin-vector action-view" action="POST" wtfarg="TEST">"""

b = """<div class="testsclass">"""

def extract_attrs(line):
    data = line[line.index("<"):line.index(">")].split(" ")
    name, data_attrs = data[0][1:], data[1:]
    attrs = {}
    for attr in data_attrs:
        if "=" in attr:
            [attr, value] = attr.split("=", 1)
            if value.startswith("\'") or value.startswith("\"") : value = value[1:]
            if value.endswith("\'") or value.endswith("\"") : value = value[:-1]
            attrs[attr] = value
        else:
            if "keywords" not in attrs.keys(): attrs["keywords"] = ""
            else : attrs["keywords"] = attr
    return name, attrs

def extract_tag_args(line):
    def keyword_args(kwargs):
        while kwargs.startswith(" "): kwargs=kwargs[1:]
        keyword = kwargs.split("=\"", 1)[0]
        args = kwargs[kwargs.index("\"")+1:]
        if args.endswith("\""):   args=args[:-1]
        elif args.endswith("\'"): args=args[:-1]
        if " " in args: args = args.split(" ")
        #print("keyword :",keyword,"\nargs    :", args)
        return keyword, args

    if line.startswith("<"): line=line[1:]
    if line.endswith("/>"):  line=line[:-2]
    elif line.endswith(">"): line=line[:-1]
    tagname = line.split(" ", 1)[0]
    line = line[line.index(" "):]
    kwargs = []
    for e in line.split("\" ") :
        kw, args = keyword_args(e)
        kwargs.append([kw, args])
    # Creating attrs dict
    attrs = {}
    for element in kwargs:
        # if len(element) == 2:
        attrs[element[0]] = element[1]
        # else:
        #     if "keywords" not in attrs.keys(): attrs["keywords"] = ""
        #     else : attrs["keywords"] += element
    return (tagname, attrs)

tagname, attrs = extract_tag_args(a)
print(tagname + " :", attrs)

tagname, attrs = extract_tag_args(b)
print(tagname + " :", attrs)