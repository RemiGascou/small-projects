#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
import pyperclip
from lib.core           import AppInfos
from lib.ui.windows     import *
from lib.ui.widgets     import *

from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *

class EmailsExtractorApp(QMainWindow):
    def __init__(self, debug=False, parent=None):
        # print("[LOG] Parent of EmailsExtractorApp", parent)
        super(EmailsExtractorApp, self).__init__()
        self._debug_   = debug
        self.title     = AppInfos.get_name()
        self.left      = 10
        self.top       = 10
        self.width     = 640
        self.height    = 200
        self.contacts_file = "/home/hermes/Downloads/contacts.csv"
        self.emails_file   = "/home/hermes/Downloads/e.txt"
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
        main_layout = QVBoxLayout()
        self.label_contacts = QLabel("<b>Input contacts CSV file :</b>", self)
        main_layout.addWidget(self.label_contacts)

        temp_widget = QWidget()
        temp_layout = QHBoxLayout()
        self.contact_path_line = QLineEdit(self)
        self.contact_path_line.textChanged.connect(lambda t:self.setText(t, self.contacts_file))
        temp_layout.addWidget(self.contact_path_line)
        self.contact_button = QPushButton("Parcourir", self)
        self.contact_button.clicked.connect(self.open_contacts_file)
        temp_layout.addWidget(self.contact_button)
        temp_widget.setLayout(temp_layout)
        main_layout.addWidget(temp_widget)

        self.label_emails = QLabel("<b>Output emails TXT file :</b>", self)
        main_layout.addWidget(self.label_emails)

        temp_widget = QWidget()
        temp_layout = QHBoxLayout()
        self.emails_path_line = QLineEdit(self)
        self.emails_path_line.textChanged.connect(lambda t:self.setText(t, self.emails_file))
        temp_layout.addWidget(self.emails_path_line)
        self.emails_button = QPushButton("Parcourir", self)
        self.emails_button.clicked.connect(self.open_emails_file)
        temp_layout.addWidget(self.emails_button)
        temp_widget.setLayout(temp_layout)
        main_layout.addWidget(temp_widget)

        self.button_convert = QPushButton("Convert", self)
        self.button_convert.clicked.connect(self.convert)
        main_layout.addWidget(self.button_convert)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        #==
        self.show()

    def _init_menu(self):
        mainMenu    = self.menuBar()
        appMenu     = mainMenu.addMenu(AppInfos.get_name())
        helpMenu    = mainMenu.addMenu('Help')

        #appMenu buttons
        openFileButton = QAction('Open Contacts File', self)
        openFileButton.triggered.connect(self.open_contacts_file)
        appMenu.addAction(openFileButton)
        openFileButton = QAction('Open Emails File', self)
        openFileButton.triggered.connect(self.open_emails_file)
        appMenu.addAction(openFileButton)
        appMenu.addSeparator()
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        appMenu.addAction(exitButton)

        #helpMenu buttons
        aboutButton = QAction('About', self)
        aboutButton.triggered.connect(self.start_AboutWindow)
        helpMenu.addAction(aboutButton)

    def convert(self):
        if len(self.contacts_file) != 0:
            f = open(self.contacts_file, "r")
            contacts_lines = f.readlines()
            f.close()

            emails = [l.split(",")[-1].replace("\n","") for l in contacts_lines[1:]]
            pyperclip.copy(';'.join(emails)+"\n")
            if len(self.emails_file) != 0:
                f = open(self.emails_file, "w")
                f.write(';'.join(emails)+"\n")
                f.close()

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("<b>%d</b> emails extraits !\nLa liste d'emails est copiée dans le presse-papier." % len(emails))
            msgBox.setWindowTitle("Information")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No CSV file given.")
            msgBox.setWindowTitle("Warning")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
        return

    def setText(self, text, var): var = text
# *------------------------------Window Handlers------------------------------ *

    def start_AboutWindow(self):
        self.wAboutWindow = AboutWindow(self)
        self.wAboutWindow.show()

    def start_none(self): return None

    def open_contacts_file(self):
        self.contacts_file = QFileDialog.getOpenFileName(self, 'OpenFile', '', "CSV files (*.csv)")[0]
        self.contact_path_line.setText(self.contacts_file)
        return None

    def open_emails_file(self):
        self.emails_file = QFileDialog.getSaveFileName(self, 'SaveFile', '', "Text files (*.txt)")[0]
        self.emails_path_line.setText(self.emails_file)
        return None

# *---------------------------------- Events --------------------------------- *

    def closeEvent(self, event):
        event.accept()
        # quit_msg = "Are you sure you want to exit the program?"
        # reply = QMessageBox.question(self, 'Exit Confirmation',
        #                 quit_msg, QMessageBox.Yes, QMessageBox.No)
        # if reply == QMessageBox.Yes: event.accept()
        # else: event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = EmailsExtractorApp(debug=True)
    sys.exit(app.exec_())
