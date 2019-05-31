#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from .Node import *

class Edge(object):
    """docstring for Edge."""
    def __init__(self, nodeStart:Node, nodeDest:Node, capacity=0, flow=0):
        super(Edge, self).__init__()
        self.nodeStart = nodeStart
        self.nodeDest  = nodeDest
        self.capacity  = capacity
        self.flow      = flow

# *----------------------------------Get Set---------------------------------- *

    def get_flow (self):
        return self.flow

    def set_flow (self, flow):
        self.flow = flow

    def get_capacity (self):
        return self.capacity

    def set_capacity (self, capacity):
        self.capacity = capacity

    def get_nodeStart(self):
        return self.nodeStart

    def get_nodeDest(self):
        return self.nodeDest

# *-----------------------------------Utils----------------------------------- *

    def __len__(self):
        return self.capacity

    def __str__(self):
        return "( " + str(self.nodeStart.get_label()) + " -> " + str(self.nodeDest.get_label()) + " : capacity=" + str(self.get_capacity()) + ", flow=" + str(self.get_flow()) + " )"
