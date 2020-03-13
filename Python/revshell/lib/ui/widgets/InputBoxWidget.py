#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class InputBoxWidget(QWidget):
    def __init__(self, parent=None):
        super(InputBoxWidget, self).__init__(parent)
        self._initUI()
        self.show()

    def _initUI(self):
        glayout = QGridLayout()
        glayout.setColumnStretch(1, 10)
        glayout.setColumnStretch(2, 1)
        self.textfield = QPlainTextEdit(self)
        glayout.addWidget(self.textfield, 1, 1)
        self.sendbutton = QPushButton('Send')
        glayout.addWidget(self.sendbutton,1,2)
        self.setLayout(glayout)

    @pyqtSlot()
    def getText(self): self.textfield
