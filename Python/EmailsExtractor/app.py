#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import sys
from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *

def appinfos_get_name() -> str:
    return "EmailsExtractor"

def appinfos_get_version() -> str:
    return "v.0.2.1"

def appinfos_get_credits() -> str:
    return "\u00A9" + "2020 - Rémi GASCOU"


class AboutWindow(QWidget):
    def __init__(self, parent=None):
        #print("[LOG] Parent of AboutWindow", parent)
        super(AboutWindow, self).__init__()
        self.title = 'About Window'
        self.left   = 0
        self.top    = 0
        self.width  = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setAttribute(Qt.WA_DeleteOnClose)  #Kill application on close
        self.setGeometry(self.left, self.top, self.width, self.height)
        self._initUI()
        self.show()

    def _initUI(self):
        self.label = QLabel("<b>" + appinfos_get_name() + " " + appinfos_get_version() + " </b><br><br>" + appinfos_get_credits(), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.setLayout(self.layout)
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('About')



class EmailsExtractorApp(QMainWindow):
    def __init__(self, debug=False, parent=None):
        # print("[LOG] Parent of EmailsExtractorApp", parent)
        super(EmailsExtractorApp, self).__init__()
        self._debug_   = debug
        self.title     = appinfos_get_name()
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
        appMenu     = mainMenu.addMenu(appinfos_get_name())
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
        if self.contacts_file != "" and self.emails_file != "":
            f = open(self.contacts_file, "r")
            contacts_lines = f.readlines()
            f.close()

            emails = [l.split(",")[-1].replace("\n","") for l in contacts_lines[1:]]

            f = open(self.emails_file, "w")
            f.write(';'.join(emails)+"\n")
            f.close()

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("%d emails extracted !" % len(emails))
            msgBox.setWindowTitle("Emails extracted")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

        else:
            pass
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
