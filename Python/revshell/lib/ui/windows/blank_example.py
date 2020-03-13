#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
RemoteConsole -> blank_example

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import AppInfos
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DebugWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.label = QLabel("<b>" + AppInfos.get_name() + " " + AppInfos.get_version() + " </b><br><br>" + AppInfos.get_credits(), self)
        self.label.setAlignment(Qt.AlignCenter)
        #self.label.setStyleSheet("QLabel {background-color: red;}")
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('About')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DebugWindow()
    sys.exit(app.exec_())
