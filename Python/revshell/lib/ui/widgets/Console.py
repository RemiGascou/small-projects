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
        self.horizontalGroupBox = QGroupBox("Grid")
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


class Console(QWidget):
    def __init__(self, host:str, port:int, parent=None):
        super(Console, self).__init__(parent)
        #Load Stylesheet from "Console.css"
        # f = open("lib/ui/widgets/styles/Console.css",'r')
        # stylesheet = "".join(f.readlines())
        # f.close()
        # self.setStyleSheet(stylesheet)
        #EndLoad
        self.chatbox = None
        self._initUI()
        self.show()

    def _initUI(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        glayout = QGridLayout()
        glayout.setRowStretch(1, 15)
        glayout.setRowStretch(2, 1)

        logOutput = QTextEdit()
        logOutput.setReadOnly(True)
        logOutput.setLineWrapMode(QTextEdit.NoWrap)
        logOutput.setStyleSheet("""QTextEdit {
            background-color: #000000;
            color: #F0F0F0;
            text-decoration: none;
            font-family: "Courier", Helvetica, sans-serif;
        }""")
        logOutput.insertPlainText('\n'.join(["[+] Remote console on :", "[+] host : "+str(self.host), "[+] port : "+str(self.port)]))
        self.setCentralWidget(logOutput)

        logOutput.moveCursor(QTextCursor.End)
        logOutput.setCurrentFont(logOutput.font())
        logOutput.setTextColor(QColor(255, 100, 100))

        logOutput.insertPlainText("LALA")

        sb = logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())


    @pyqtSlot()
    def addText(self):
        self.chatbox.appendHtml("Smiley test ! &#9762; &#9749;")

    def addHTML(self, htmltext):
        self.chatbox.appendHtml(htmltext)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
