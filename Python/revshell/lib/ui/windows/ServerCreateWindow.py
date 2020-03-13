#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
RemoteConsole -> ServerCreateWindow

Author: Remi GASCOU
Last edited: July 2018
"""

import sys
from lib.core import *

from lib.core.data.ServerInfos import *
from lib.core.server.Server import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ServerCreateWindow(QWidget):
    def __init__(self, parent=None):
        #print("[LOG] Parent of ServerCreateWindow", parent)
        super(ServerCreateWindow, self).__init__()
        self.setWindowTitle('Create Server')
        #self.setGeometry(300, 300, 300, 175)
        self.setFixedSize(300, 175)
        self._initUI()
        self.show()

    def _initUI(self):
        #form
        self.formWidget = QWidget(self)
        self.formlayout = QFormLayout()
        self.entry_server_name = QLineEdit()
        self.formlayout.addRow("Server Name", self.entry_server_name)
        self.entry_server_port = QLineEdit()
        self.entry_server_port.setInputMask('99999')
        self.formlayout.addRow("Server Port", self.entry_server_port)
        self.checkbox_password = QCheckBox()
        self.checkbox_password.clicked.connect(self._checkbox_password_Event)
        self.formlayout.addRow("Define Password", self.checkbox_password)
        self.entry_server_password = QLineEdit()
        self.entry_server_password.setEnabled(False)
        self.formlayout.addRow("Password", self.entry_server_password)
        self.formWidget.setLayout(self.formlayout)
        #end form

        self.submitbutton = QPushButton("Create Server", self)
        self.submitbutton.clicked.connect(self.submitCreate)
        self.layout = QGridLayout()
        self.layout.addWidget(self.formWidget, 0, 0)
        self.layout.addWidget(self.submitbutton, 1, 0)
        self.setLayout(self.layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.submitCreate()

    @pyqtSlot()
    def submitCreate(self):
        si = ServerInfos()
        if len(self.entry_server_name.text()) > 0 and self.entry_server_name.text().isalnum():
            si.set_name(self.entry_server_name.text())
        if len(self.entry_server_port.text()) > 0 and self.entry_server_port.text().isnum():
            si.set_port(self.entry_server_port.text())
        if len(self.entry_server_password.text()) > 0 and self.entry_server_password.text().isalnum():
            si.set_password(self.entry_server_password.text())
        print(si)
        serverthread = Server(si)
        serverthread.start()
        self.destroy()


    @pyqtSlot()
    def _checkbox_password_Event(self):
        print("Toggle", self.checkbox_password.isChecked())
        if self.checkbox_password.isChecked() :
            self.entry_server_password.setEnabled(True)
        else:
            self.entry_server_password.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ServerCreateWindow()
    sys.exit(app.exec_())
