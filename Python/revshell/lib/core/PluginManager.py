#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
import glob

class PluginManager(object):
    """docstring for PluginManager."""

    def __init__(self, debug=True):
        super(PluginManager, self).__init__()
        self._debug_           = debug
        self.available_plugins = []
        self.loaded_plugins    = []
        self._generate_available_plugins()

    def debug(self, message):
        if self._debug_ :
            print("\x1b[1m[\x1b[93mdebug\x1b[0m\x1b[1m]\x1b[0m \x1b[94m"+__name__+"\x1b[0m : "+message)
        return None

    def detect_plugins(self):
        plugins = []
        for file in __import__('glob').glob("./lib/plugins/*.py"):
            f = open(file, "r")
            content = [line for line in f.readlines() if "class " in line and "RevShellPlugin" in line]
            f.close()
            if len(content) != 0:
                plugin_name = content[0].split("class ")[1].replace(" ","").split("(RevShellPlugin)")[0]
                plugins.append(plugin_name)
        if self._debug_ == True :
            if len(plugins) == 0:
                self.debug("No detected plugin.")
            else:
                self.debug("Detected plugins (%d) :" % len(plugins))
                for p in plugins[:-1] : self.debug("  ├── "+p)
                self.debug("  └── "+plugins[-1])
        detected_plugins = sorted(plugins)
        self.write_init_plugins(detected_plugins)
        return detected_plugins

    def write_init_plugins(self, detected_plugins):
        """Documentation for write_init_plugins"""
        self.debug("Creating plugins/__init__.py")
        f = open("./lib/plugins/__init__.py", "w")
        f.write("#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\n")
        for p_name in detected_plugins:
            f.write("from ."+p_name+" import *\n")
        f.close()

    def _generate_available_plugins(self):
        """Documentation for _generate_available_plugins"""
        self.available_plugins = []
        detected_plugins = self.detect_plugins()
        for p_name in detected_plugins:
            self.available_plugins.append((p_name, self.str_to_class(p_name)))
        return

    def load_plugin(self, plugin:str):
        """Documentation for load_plugins"""
        plugin_names = [p[0] for p in self.available_plugins]
        if plugin in plugin_names:
            self.loaded_plugins.append((plugin, self.str_to_class(plugin)(debug=self._debug_)))
        else:
            self.debug("Cannot find plugin " + plugin)
        return self.loaded_plugins

    def load_plugins(self, plugins:list):
        """Documentation for load_plugins"""
        for p_name in plugins:
            if type(p_name) == str:
                self.load_plugin(p_name)
        return self.loaded_plugins

    def load_all_plugins(self):
        """Documentation for load_plugins"""
        plugins = [p[0] for p in self.available_plugins]
        self.debug("Loading plugins : " + str(plugins))
        return self.load_plugins(plugins)

    def str_to_class(self, classname):
        """Documentation for str_to_class"""
        try:
            out = getattr(sys.modules[__name__], classname)
        except Exception as e:
            out = None
        return out

p = PluginManager(debug=False)
del p
from ..plugins import *
