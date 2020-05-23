#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> myUI_server.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 17:14
@Desc    :
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from ui_server import Ui_MainWindow


class QmyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyMainWindow()
    form.show()
    sys.exit(app.exec_())
