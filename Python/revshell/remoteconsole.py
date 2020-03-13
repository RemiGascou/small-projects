#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

# Une remote console ssh pour revshell,
# avec une mini interface graphique (un bouton upload file)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument('-t','--target', required=True, type=str, help='Target remote host.')
    parser.add_argument('-p', '--port',  required=True, type=int, help='Port')
    parser.add_argument('-d', '--debug', required=False, action='store_const', const=True, default=False, help='Enable debug mode.')
    args = parser.parse_args()

    import os, sys
    from PyQt5.QtWidgets    import *
    from PyQt5.QtGui        import *
    from PyQt5.QtCore       import *

    from lib import *

    app = QApplication(sys.argv)
    ex  = RemoteConsoleApp(args.target, args.port, debug=args.debug)
    sys.exit(app.exec_())
