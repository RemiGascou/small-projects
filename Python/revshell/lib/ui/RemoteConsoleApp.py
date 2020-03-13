#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from lib.core           import AppInfos
from lib.ui.windows     import *
from lib.ui.widgets     import *
from lib.core.PluginManager import *
from lib.plugins        import *
from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *

class RemoteConsoleApp(QMainWindow):
    def __init__(self, host:str, port:int, debug=False, parent=None):
        # print("[LOG] Parent of RemoteConsoleApp", parent)
        super(RemoteConsoleApp, self).__init__()
        self._debug_   = debug
        self.title     = AppInfos.get_name() + " : " + host
        self.left      = 10
        self.top       = 10
        self.width     = 640
        self.height    = 400
        self.host      = str(host)
        self.port      = max(min(65535, int(port)), 0)
        self.w_console = None
        # Plugins
        self.pluginManager  = PluginManager(debug=self._debug_)
        self.plugins        = self.pluginManager.load_all_plugins()
        self._initUI()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout().setContentsMargins(0,0,0,0)
        self.setAttribute(Qt.WA_DeleteOnClose)
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self._init_menu()
        #==
        self.w_console = ConsoleWidget(self.host, self.port, debug=self._debug_)
        self.setCentralWidget(self.w_console)
        #==
        self.show()

    def _init_menu(self):
        mainMenu    = self.menuBar()
        appMenu     = mainMenu.addMenu(AppInfos.get_name())
        targetMenu  = mainMenu.addMenu('Target')
        pluginsMenu = mainMenu.addMenu('Plugins')
        helpMenu    = mainMenu.addMenu('Help')

        #appMenu buttons
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        appMenu.addAction(exitButton)

        #targetMenu buttons
        reconnectButton = QAction('Reconnect', self)
        reconnectButton.setStatusTip('Reconnect to target')
        reconnectButton.triggered.connect(self.console_reconnect)
        targetMenu.addAction(reconnectButton)

        #pluginsMenu buttons
        pluginManagerButton = QAction('PluginManager', self)
        pluginManagerButton.setStatusTip('Exit application')
        pluginManagerButton.triggered.connect(self.start_none)
        pluginsMenu.addAction(pluginManagerButton)
        pluginsMenu.addSeparator()

        for (plugin_name, plugin) in self.plugins:
            pluginsMenu.addMenu(plugin.menu_entry(pluginsMenu))


        #helpMenu buttons
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.start_AboutWindow)
        helpMenu.addAction(aboutButton)
        helpMenu.addSeparator()
        debugButton = QAction('Debug', self)
        debugButton.triggered.connect(self.start_DebugWindow)
        helpMenu.addAction(debugButton)

# *------------------------------Window Handlers------------------------------ *

    def start_AboutWindow(self):
        self.wAboutWindow = AboutWindow(self)
        self.wAboutWindow.show()

    def start_DebugWindow(self):
        self.wDebugWindow = DebugWindow(self)
        self.wDebugWindow.show()

    def console_reconnect(self): self.w_console.reconnect()

    def start_none(self): return None

# *---------------------------------- Events --------------------------------- *

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Exit Confirmation',
                        quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.w_console.close()
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = RemoteConsoleApp(debug=True)
    sys.exit(app.exec_())
