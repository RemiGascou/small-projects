# -*- coding: utf-8 -*-

from lib import *

if __name__ == '__main__':
    f = open("out.html", "r")
    html = '\n'.join(f.readlines())
    f.close()

    hp = HTMLParser(html)

    f = open("out_pretty.html", "w")
    for line in hp.htmltext:
        f.write(line+"\n")
    f.close()
    # print(hp.autoindent(), "\n\n")

    p = hp.parse(log=False)
    # print("\n\n")
    # for e in p:
    #     print(e)

    #print(hp.find_by_tag("h1"))

    #print(hp.find_by_property("itemprop"))

    print(hp.find_by_property("itemprop", value="givenName"))
