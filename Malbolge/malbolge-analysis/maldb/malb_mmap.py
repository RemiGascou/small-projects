# -*- coding: utf-8 -*-

class malb_mmap(object):
    """docstring for malb_mmap."""
    def __init__(self):
        super(malb_mmap, self).__init__()
        self.allocatedcells = 1
        self.mem = {"0t0000000000":0}

    def printmem(self):
        for addr in self.mem:
            print("[" + addr + "] :",self.mem[addr])

    def expand_addr(self,mem_addr):
        if self.isValid(mem_addr):
            if len(mem_addr[:2]) < 10:
                mem_addr = mem_addr[:2] + mem_addr[2:].rjust(10,"0")
            return mem_addr

    def reduce_addr(self,mem_addr):
        if self.isValid(mem_addr):
            if len(mem_addr[:2]) < 10:
                mem_addr = mem_addr[:2] + mem_addr[2:].rjust(10,"0")
            return mem_addr

    def isValid(self, mem_addr):
        outcome = True
        if mem_addr.startswith("0t") and len(mem_addr) <= 12:
            mem_addr = mem_addr[:2]
            if len(mem_addr) < 10:
                mem_addr = mem_addr.rjust(10,"0")
            for c in mem_addr:
                if c not in ["0","1","2"]:
                    outcome = False
        return outcome

    def __iter__(self):
        pass

    def __str__(self):
        pass

    def __getitem__(self,mem_addr):
        mem_addr = str(mem_addr)
        if mem_addr in self.mem.keys():
            return self.mem[self.expand_addr(mem_addr)]
        else:
            raise IndexError

    def __setitem__(self,mem_addr, value):
        mem_addr = str(mem_addr)
        if self.isValid(mem_addr):
            self.mem[self.expand_addr(mem_addr)] = int(str(max(min(value, 0), 59032)), base=3)
        else:
            raise IndexError

if __name__ == '__main__':
    malbmem = malb_mmap()
