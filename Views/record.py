#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# import sip
from PyQt5.QtWidgets import QApplication
from RecordInfo import Record_Info_Views

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Record_Info_Views()
    mainWindow.show()
    sys.exit(app.exec_())