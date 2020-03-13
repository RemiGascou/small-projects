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

class Jerome(RevShellPlugin):
    """ RevShell Plugin Jerome. """
    def __init__(self, debug=False):
        super(RevShellPlugin, self).__init__()
        self._debug_         = debug
        self.plugin_name     = __name__.split(".")[-1]
        self.debug(__name__, "Loading plugin ")

    def menu_entry(self, parent_menu):
        self.debug(__name__, "Configuring menu entry Plugins->"+self.plugin_name)
        p_menu = QMenu(self.plugin_name, parent_menu)
        JeromeButton = QAction('Jerome Button', p_menu)
        JeromeButton.setStatusTip('If you see this, it means it works')
        JeromeButton.triggered.connect(lambda x : print("Clicked Jerome button"))
        p_menu.addAction(JeromeButton)
        return p_menu
