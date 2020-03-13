#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

# import datetime
import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from lib.core.Client import *
from lib.ui.widgets  import *

class ConsoleWidget(QWidget):
    def __init__(self, host:str, port:int, parent=None, debug=False):
        super(ConsoleWidget, self).__init__(parent)
        self._debug_     = debug
        self.host        = str(host)
        self.port        = max(min(65535, int(port)), 0)
        self.refreshTime = 50 # in ms
        #=========================================
        self.client = None
        self.connect()
        self._initUI()
        self.updateTimer = QTimer()
        self.updateTimer.timeout.connect(self.update_content)
        self.updateTimer.start(self.refreshTime)

    def _initUI(self):
        self.text_output = QPlainTextEdit()
        self.text_output.setReadOnly(True)
        self.text_output.setStyleSheet("""QPlainTextEdit {
            background-color: #000000;
            color: #F0F0F0;
            text-decoration: none;
            font-family: "Courier", Helvetica, sans-serif;
        }""")
        self.text_output.insertPlainText('\n'.join(["[+] Remote shell on :", "[+] Host : "+str(self.host), "[+] Port : "+str(self.port), "", ""]))
        self.text_output.moveCursor(QTextCursor.End)
        glayout = QGridLayout()
        glayout.setContentsMargins(0,0,0,0)
        glayout.addWidget(self.text_output, 0, 0)
        self.setLayout(glayout)

    def update_content(self):
        """Documentation for update_content"""
        data = self.client.read()
        if len(data) > 0:
            self.text_output.moveCursor(QTextCursor.End)
            for line in data.replace("\r", "").split("\n"):
                if len(line) > 0:
                    # print(bytes(line, "UTF-8"))
                    if line not in [self.client.msgs[key] for key in self.client.msgs]:
                         if set(line) != [" "]:
                            # self.text_output.appendHtml("<b>[prompt]$</b> (")
                            self.text_output.insertPlainText("[prompt]$ (" + line + ")"+"\n")
                    else:
                        tf = QTextCharFormat()
                        self.text_output.currentCharFormat()
                        tf.setForeground(QColor(255,0,0))
                        self.text_output.setCurrentCharFormat(tf)
                        self.text_output.insertPlainText(line + "\n")
        return len(data)

    def connect(self):
        """Documentation for reconnect"""
        self.client = Client(self.host, self.port, debug=self._debug_)
        self.client.start()

    def reconnect(self):
        """Documentation for reconnect"""
        self.connect()

    def close(self):
        """Documentation for close"""
        self.client.stop()
