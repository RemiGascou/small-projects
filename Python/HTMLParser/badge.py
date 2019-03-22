
def fname(arg):
    pass

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
html = """<html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
</body>
</html>""" #the HTML code you've written above
parsed_html = BeautifulSoup(html)
print(parsed_html.body.find('div', attrs={'class':'container'}).text)
