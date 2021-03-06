# HTMLParser

## Methods :

```
autoindent()        : Autoindent the HTML code provided
findall_tags(tag)   : Extracts content between inside a tag.
parse()             : Generates a table used for searching (used by findall_tags()...)
```


## Examples :

### Autoindent

```python
from lib import *

html = """<html><head>Heading</head><body attr1='val1'><div class='container'><div id='id#01'>Something here</div><div id="id#02">Something else</div></div></body></html>"""

hp = HTMLParser(html)
# Autoindent
print(hp.autoindent(), "\n\n")
```

Output :
```
<html>
    <head>
        Heading
    </head>
    <body attr1='val1'>
        <div class='container'>
            <div id='id#01'>
                Something here
            </div>
            <div id="id#02">
                Something else
            </div>
        </div>
    </body>
</html>
```

### Find by tag

```python
from lib import *

html = """<html><head>Heading</head><body attr1='val1'><div class='container'><div id='id#01'>Something here</div><div id="id#02">Something else</div></div></body></html>"""

hp = HTMLParser(html)

# Parsing
p = hp.parse()

# Searching div :
print(hp.findall_tags("div"))
```
