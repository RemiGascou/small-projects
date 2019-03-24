# -*- coding: utf-8 -*-

from lib import *

if __name__ == '__main__':
    html = """<html><head>Heading</head><body attr1='val1'><div class='container'><div id='id#01'>Something here</div><div id="id#02">Something else</div></div></body></html>"""

    f = open("out.html", "r")
    html = '\n'.join(f.readlines())
    f.close()

    hp = HTMLParser(html)
    # print(hp.autoindent(), "\n\n")

    p = hp.parse()
    # print("\n\n")
    # for e in p:
    #     print(e)

    print(hp.findall_tags("div"))
