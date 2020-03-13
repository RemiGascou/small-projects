#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

from PyQt5.QtWidgets       import *
from PyQt5.QtGui           import *
from PyQt5.QtCore          import *
from ..core.RevShellPlugin import *

class TestPlugin(RevShellPlugin):
    """ RevShell Plugin TestPlugin. """
    def __init__(self, debug=False):
        super(RevShellPlugin, self).__init__()
        self._debug_         = debug
        self.plugin_name     = __name__.split(".")[-1]
        self.debug(__name__, "Loading plugin ")

    def menu_entry(self, parent_menu):
        self.debug(__name__, "Configuring menu entry Plugins->"+self.plugin_name)
        p_menu = QMenu(self.plugin_name, parent_menu)
        testButton_01 = QAction('TestPlugin Button', p_menu)
        testButton_01.setStatusTip('If you see this, it means it works')
        testButton_01.triggered.connect(lambda x : print("Clicked TestPlugin button"))
        p_menu.addAction(testButton_01)

        testButton_02 = QAction('testButton_02 Button', p_menu)
        testButton_02.triggered.connect(lambda x : print("Clicked testButton_02 button"))
        p_menu.addAction(testButton_02)

        p_menu.addSeparator()

        testButton_03 = QAction('testButton_03 Button', p_menu)
        testButton_03.triggered.connect(lambda x : print("Clicked testButton_03 button"))
        p_menu.addAction(testButton_03)
        return p_menu
