#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             : Remi GASCOU
# Date created       :
# Date last modified :
# Python Version     : 3.*

from .Edge import *
from .Node import *

class Graph(object):
    """docstring for Graph."""
    def __init__(self, listOfNodeLabels=[], listOfEdges=[]):
        super(Graph, self).__init__()
        if len(listOfNodeLabels) != 0:
            if type(listOfNodeLabels[0]) == str: nodes = [Node(labelstr) for labelstr in listOfNodeLabels if type(labelstr) == str]
            elif type(listOfNodeLabels[0]) == int: nodes = [Node(labelint) for labelint in listOfNodeLabels if type(labelint) == int]
            elif type(listOfNodeLabels[0]) == Node: nodes = [node for node in listOfNodeLabels if type(node) == Node]
            if len(nodes) == len(listOfNodeLabels): self.nodes = nodes
            else: self.nodes = []
        else: self.nodes = []
        self.edges = []

        if len(listOfEdges) != 0:
            edges = []
            if type(listOfEdges[0]) == Edge: edges = [edge for edge in listOfEdges if type(edge) == Edge]
            elif len(listOfEdges[0]) == 2 and type(listOfEdges[0]) == list and type(listOfEdges[0][0]) == str and type(listOfEdges[0][1]) == str:
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest))
                if len(edges) == len(listOfEdges): self.edges = edges
            elif len(listOfEdges[0]) == 3 and type(listOfEdges[0]) == list and type(listOfEdges[0][0]) == str and type(listOfEdges[0][1]) == str and (type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float):
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2]))
                if len(edges) == len(listOfEdges): self.edges = edges
            elif len(listOfEdges[0]) == 3 and type(listOfEdges[0]) == list and type(listOfEdges[0][2]) == int and type(listOfEdges[0][2]) == int and type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float:
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2]))
            elif len(listOfEdges[0]) == 4 and (type(listOfEdges[0]) == list) and (type(listOfEdges[0][0]) == str) and (type(listOfEdges[0][1]) == str) and (type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float) and (type(listOfEdges[0][3]) == int or type(listOfEdges[0][3]) == float):
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2], flow=edge[3]))
            elif len(listOfEdges[0]) == 4 and type(listOfEdges[0]) == list and (type(listOfEdges[0][2]) == int) and (type(listOfEdges[0][2]) == int) and (type(listOfEdges[0][2]) == int or type(listOfEdges[0][2]) == float) and (type(listOfEdges[0][3]) == int or type(listOfEdges[0][3]) == float):
                edges = []
                for edge in listOfEdges:
                    nodeStart = self.get_node_by_label(edge[0])
                    nodeDest  = self.get_node_by_label(edge[1])
                    if nodeStart != None and nodeDest != None : edges.append(Edge(nodeStart, nodeDest, capacity=edge[2], flow=edge[3]))

        self.nodestable = {}
        for node in self.nodes :
            self.nodestable[node.get_label()] = []

# *----------------------------------Get Set---------------------------------- *

    def get_nodes (self):
        return self.nodes

    def get_node_by_label (self, label):
        for node in self.nodes:
            if node.get_label() == label:
                return node
        return None

    def get_edges (self):
        return self.edges

    def add_edges (self, nodeStart, nodeDest):
        self.edges.append(Edge(nodeStart, nodeDest))
        if nodeDest.get_label() not in self.nodestable[nodeStart.get_label()]:
            self.nodestable[nodeStart.get_label()].append(nodeDest.get_label())

    def add_node (self, nodeOrLabel):
        if type(nodeOrLabel) == Node:
            self.nodes.append(nodeOrLabel)
        elif type(nodeOrLabel) == str:
            self.nodes.append(Node(nodeOrLabel))

# *-----------------------------------Utils----------------------------------- *

    def __len__(self):
        return len(self.nodes), len(self.edges)
