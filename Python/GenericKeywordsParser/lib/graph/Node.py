#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : 
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

class Node(object):
    """docstring for Node."""
    def __init__(self, label, description=""):
        super(Node, self).__init__()
        self.label       = label
        self.description = description

    def get_label(self):
        return self.label

    def get_description(self):
        if len(self.description) != 0:
            return self.description
        elif len(self.description) == 0:
            return self.label

    def __str__(self):
        return str(self.label)
