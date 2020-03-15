#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets    import *
    from PyQt5.QtGui        import *
    from PyQt5.QtCore       import *

    from lib import *

    app = QApplication(sys.argv)
    ex  = EmailsExtractorApp(debug=True)
    sys.exit(app.exec_())
