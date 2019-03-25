# -*- coding: utf-8 -*-


#push_message = "\x1b[1m[\x1b[93mPUSH\x1b[0m\x1b[1m]\x1b[0m"
push_message = "[PUSH]"
#pop_message  = "\x1b[1m[\x1b[92mPOP_\x1b[0m\x1b[1m]\x1b[0m"
pop_message = "[POP_]"


class Stack(object):
    """docstring for Stack."""
    def __init__(self, log=False):
        super(Stack, self).__init__()
        self.stack = []
        self._log = log

    def push(self, element, log=False):
        log = self._log or log
        self.stack.append(element)
        if log: print(push_message, self.stack[-1])

    def top(self):
        log = self._log or log
        if len(self.stack) != 0:
            if log: print("[TOP:]", self.stack[-1])
            return self.stack[-1]
        else:
            print("[WARN] Stack is empty.")
        return None

    def pop(self, element, log=False):
        log = self._log or log
        if len(self.stack) != 0:
            if self.stack[-1] != element:
                print("[WARN] First element of the stack is \"" + self.stack[-1] +"\" and not \"" + element + "\"")
                return None
            else:
                pop_element = self.stack[-1]
                self.stack = self.stack[:-1]
                if log: print(pop_message, pop_element)
                return pop_element
        else:
            return None

    def currentstack(self):
        strstack = [str(e) for e in self.stack]
        if len(strstack) != 0:
            maxlen = max([len(e) for e in strstack])
            return '\n'.join(["|" + e.center(maxlen, " ") + "|" for e in strstack[::-1]]) + "\n|" + "_"*maxlen + "|"
        else:
            return "\n|_EMPTY_STACK_|"



if __name__ == '__main__':
    s = Stack(True)
    s.push("obj")
    #print(s.currentstack())

    s.push("stream")
    #print(s.currentstack())
    s.top()

    s.pop("stream")
    s.pop("obj")
