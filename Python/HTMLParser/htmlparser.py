



class HTMLParser(object):
    """docstring for HTMLParser."""
    def __init__(self, htmltext):
        def rmsep(s):
            while s.startswith(" ") or  s.startswith("\t") : s=s[1:]
            return s
        super(HTMLParser, self).__init__()
        self.htmltext = [rmsep(line) for line in htmltext.replace("</", "\n</").replace(">\n", ">\n").split("\n") if rmsep(line) != "\n"]

    def parse(self) :
        for e in self.htmltext :
            print(e)






if __name__ == '__main__':
    html = """<html>
    <head>Heading</head>
    <body attr1='val1'>
        <div class='container'>
            <div id='class'>Something here</div>
            <div>Something else</div>
        </div>
    </body>
    </html>"""

    hp = HTMLParser(html)
    hp.parse()
