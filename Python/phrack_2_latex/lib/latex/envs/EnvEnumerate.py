# -*- coding: utf-8 -*-

class EnvEnumerate(object):
    """docstring for EnvEnumerate."""

    def __init__(self):
        super(EnvEnumerate, self).__init__()
        self.items = []
        self._itemtypes = {
            "-" : "\\item ",
            "custom" : ""
        }
        self.item_type = "-"

    def export_latex(self):
        """Documentation for export"""
        multilinesep = "\n\t" + "\t"*(len(self._itemtypes[self.item_type])//4) + " "*(len(self._itemtypes[self.item_type])%4)
        texdata = "\\begin{enumerate}\n"
        for item in self.items:
            texdata += "\t"+ self._itemtypes[self.item_type] + multilinesep.join(item.split("\n")) + "\n"
        texdata += "\\end{enumerate}\n\n"
        return texdata

    def set_item_type(self, new_item_type="-"):
        if new_item_type in self._itemtypes.keys():
            self.item_type = new_item_type
        else:
            self.item_type = "custom"
            self._itemtypes["custom"] = new_item_type

    def get_item_type(self):
        return self.item_type

    def append(self, newitem):
        self.items.append(newitem)

    def __getitem__(self,index):
        out = None
        try:
            out = self.items[index]
        except IndexError as e:
            raise IndexError("")
        return out


if __name__ == '__main__':
    eit = EnvEnumerate()
    eit.append("Salut c'est moi")
    eit.append("Lorem ipsum dolor sit amet, consectetur adipisicing elit, \nSed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    eit.set_item_type("-")
    print(eit.export_latex())
