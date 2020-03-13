#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

class RevShellPlugin(object):
    """docstring for RevShellPlugin."""

    def __init__(self, root_window=None, debug=True):
        super(RevShellPlugin, self).__init__()
        self._debug_        = debug
        self._root_window   = root_window

    def menu_entry(self, parent_menu):
        """Documentation for menu_entry"""
        return None

    def debug(self, name, message):
        """Documentation for debug"""
        if self._debug_ : print("\x1b[1m[\x1b[93mdebug\x1b[0m\x1b[1m]\x1b[0m \x1b[94m"+name+"\x1b[0m : "+message)
        return None
