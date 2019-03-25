# -*- coding: utf-8 -*-


#push_message = "\x1b[1m[\x1b[93mPUSH\x1b[0m\x1b[1m]\x1b[0m"
push_message = "[PUSH]"
#pop_message  = "\x1b[1m[\x1b[92mPOP_\x1b[0m\x1b[1m]\x1b[0m"
pop_message = "[POP_]"


class Stack(object):
    """docstring for Stack."""
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def push(self, name, linein, attrs={}, log=False):
        data = {
            "name"      : name,
            "linein"    : linein,
            "lineout"   : -1,
            "attrs"     : attrs
        }
        self.stack.append(data)
        if log: print(push_message, self.stack[-1])

    def pop(self, name, lineout, log=False):
        if len(self.stack) != 0:
            if self.stack[-1]["name"] != name:
                print("[WARN] First element of the stack is \"" + self.stack[-1]["name"] +"\" and not \"" + name + "\"")
                return None
            else:
                data = self.stack[-1]
                data["lineout"] = lineout
                self.stack = self.stack[:-1]
                if log: print(pop_message, data)
                return data
        else:
            return None

    def currentstack(self):
        stack_el_names = [e["name"] for e in self.stack]
        if len(stack_el_names) != 0:
            maxlen = max([len(e) for e in stack_el_names])
            return '\n'.join(["|" + name.center(maxlen, " ") + "|" for name in stack_el_names[::-1]]) + "\n|" + "_"*maxlen + "|"
        else:
            return "\n|_EMPTY_STACK_|"






if __name__ == '__main__':
    s = Stack()
    s.push("html", 0)
    s.push("head", 1)
    print(s.pop("html", 3))
    print(s.pop("head", 3))
