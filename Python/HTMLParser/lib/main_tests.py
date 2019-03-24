from HTMLParser import *

def sectionheader(header):
    print("\x1b[1m"+ (" " + header + " ").center(50, "=") + "\x1b[0m")

def testoutcome(name, outcome):
    maxlen = 30
    if len(name) > maxlen: name = name[:maxlen]
    else: name = name.ljust(maxlen, " ")
    if outcome == True: print(" - "+name+"\x1b[1m[\x1b[92mPASSED\x1b[0m\x1b[1m]\x1b[0m")
    else : print(" - "+name+"\x1b[1m[\x1b[91mFAILED\x1b[0m\x1b[1m]\x1b[0m")

# ==============================================================================

def testcase_indentation():
    testoutcome("testT", True)
    testoutcome("testF", False)



if __name__ == '__main__':
    html = ""
    hp = HTMLParser(html)
    sectionheader("Indentation")
    testcase_indentation()
