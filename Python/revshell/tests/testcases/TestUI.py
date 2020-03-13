# -*- coding: utf-8 -*-

import os, sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib import *

class TestUI(object):
    """docstring for TestUI."""
    def __init__(self, tc):
        super(TestUI, self).__init__()
        self.tc = tc

    def test(self):
        print("\x1b[1m" + " Testing UI ".center(80, "-") + "\x1b[0m")
        if self.tc.xdisplay :
            self.tc.test("RemoteConsole main UI", self._test_AppUI)
            self.tc.test("AboutWindow", self._test_AboutWindow)
            self.tc.test("DebugWindow", self._test_DebugWindow)
            self.tc.test("ClientConnectWindow", self._test_ClientConnectWindow)
            self.tc.test("ServerCreateWindow", self._test_ServerCreateWindow)
        else :
            self.tc.test("No X display found", self._test_pass)

    def _test_AppUI(self):
        passed = True
        # try :
        #     app = QApplication(sys.argv)
        #     ex = RemoteConsoleApp()
        #     ex.close()
        # except Exception:
        #     passed = False
        return passed

    def _test_AboutWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = AboutWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_DebugWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = DebugWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_ClientConnectWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = ClientConnectWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_ServerCreateWindow(self):
        passed = True
        try :
            app = QApplication(sys.argv)
            ex = ServerCreateWindow()
            ex.close()
        except Exception:
            passed = False
        return passed

    def _test_pass(self):
        passed = True
        return passed
