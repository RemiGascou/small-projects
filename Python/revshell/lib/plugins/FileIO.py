#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import os
import base64

from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from ..core.RevShellPlugin import *

class FileIO(RevShellPlugin):
    """
    RevShell Plugin FileIO.
    """

    def __init__(self, debug=False):
        super(RevShellPlugin, self).__init__()
        self._debug_         = debug
        self._root_window    = None
        self.plugin_name     = __name__.split(".")[-1]
        self.debug(__name__, "Loading plugin ")
        self.local_filename  = ""
        self.remote_filename = ""
        self.chunk_size      = 50

    def menu_entry(self, parent_menu):
        self.debug(__name__, "Configuring menu entry Plugins->"+self.plugin_name)
        p_menu = QMenu(self.plugin_name, parent_menu)
        fileUploadButton = QAction('Upload File', p_menu)
        fileUploadButton.setShortcut('Ctrl+U')
        fileUploadButton.setStatusTip('Upload File')
        fileUploadButton.triggered.connect(self.window_uploadFile)
        p_menu.addAction(fileUploadButton)
        return p_menu

    def window_uploadFile(self):
        """Documentation for uploadFile"""
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        self.debug("Uploading "+filename)
        self.upload(filename, filename)
        return None

    def upload(self, local_filename, remote_filename):
        """
        Documentation for upload
        local_filename ==> remote_filename
        """
        self.local_filename, self.remote_filename = local_filename, remote_filename
        self.debug("Uploading "+self.local_filename+" ===> "+self.remote_filename)
        if os.path.isfile(self.local_filename) == True:
            f = open(self.local_filename, "rb")
            data = b'\n'.join(f.readlines())
            f.close()
            b64data = base64.b64encode(data).decode("ISO-8859-1")
            chunks  = [b64data[self.chunk_size*k:self.chunk_size*(k+1)] for k in range(len(b64data)//self.chunk_size)]+[b64data[self.chunk_size*(len(b64data)//self.chunk_size):]]
            for c in chunks: print(" echo \""+c+"\" >> .tmp."+self.remote_filename+".b64;")
            print(" cat .tmp."+self.remote_filename+".b64 | base64 -d > "+file+"; rm .tmp."+self.remote_filename+".b64")
            print(" chmod "+oct(os.stat(self.local_filename).st_mode)[-3:]+" "+file)
            if os.access(self.local_filename, os.X_OK) : print(" chmod +x "+file)
        return None

    def download(self, local_filename, remote_filename):
        """
        Documentation for download
        local_filename <== remote_filename
        """
        self.local_filename, self.remote_filename = local_filename, remote_filename
        # TODO: Here
        if self.debug == True : print("[DOWNLOAD] ",self.local_filename,"<==",self.remote_filename)
        f = open(self.local_filename, "wb")
        data = '\n'.join(f.readlines())
        f.close()
        return

# *----------------------------------Get Set---------------------------------- *

    def get_filename (self):
        return self.local_filename

    def set_filename (self, local_filename):
        if type(self.local_filename) == str:
            self.local_filename = local_filename
        return self

    def get_filename (self):
        return self.remote_filename

    def set_filename (self, remote_filename):
        if type(self.remote_filename) == str:
            self.remote_filename = remote_filename
        return self

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" file")
    else :
        file = sys.argv[1]
        f = FileIO()
        f.upload(file, "target.file")
