#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> myUI_server.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 17:14
@Desc    :标题栏参考链接：https://blog.csdn.net/qq_37386287/article/details/87900403
@Version : 0.0.0.1 --> 2020/05/25 --> 目前可以写出标题栏，但是标题栏和上半部分有些许空隙,另外手动拉动窗体大小，可以往右拉长，但是在往左拉就不行了。
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt, QSize, QRect
from ui_server_widget import Ui_Form

# 按钮高度
BUTTON_HEIGHT = 30
# 按钮宽度
BUTTON_WIDTH = 30
# 标题栏高度
TITLE_HEIGHT = 30


class TitleWidget(QWidget):
    def __init__(self):
        super().__init__()
        # titleIcon = QPixmap("./resource/img/icon.jpg")
        # Icon = QLabel()
        # Icon.setPixmap(titleIcon.scaled(25, 25))
        titleContent = QLabel("标题内容")
        titleContent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        titleContent.setFixedHeight(TITLE_HEIGHT)
        titleContent.setObjectName("TitleContent")
        self.ButtonMin = QPushButton("-")
        self.ButtonMin.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.ButtonMin.setObjectName("ButtonMin")
        self.ButtonMax = QPushButton("口")
        self.ButtonMax.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.ButtonMax.setObjectName("ButtonMax")
        self.ButtonRestore = QPushButton("回")
        self.ButtonRestore.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.ButtonRestore.setObjectName("ButtonRestore")
        self.ButtonRestore.setVisible(False)
        self.ButtonClose = QPushButton("×")
        self.ButtonClose.setFixedSize(QSize(BUTTON_WIDTH, BUTTON_HEIGHT))
        self.ButtonClose.setObjectName("ButtonClose")
        mylayout = QHBoxLayout()
        mylayout.setSpacing(0)
        mylayout.setContentsMargins(0, 0, 0, 0)
        # mylayout.addWidget(Icon)

        mylayout.addWidget(titleContent)
        mylayout.addWidget(self.ButtonMin)
        mylayout.addWidget(self.ButtonMax)
        mylayout.addWidget(self.ButtonRestore)
        mylayout.addWidget(self.ButtonClose)

        self.setLayout(mylayout)

        # 使用qss渲染
        with open("./resource/QSS/title_style1.qss") as f:
            qss = f.read()
        self.setStyleSheet(qss)

        self.restorePos = None
        self.restoreSize = None
        self.startMovePos = None

    def saveRestoreInfo(self, point, size):
        self.restorePos = point
        self.restoreSize = size

    def getRestoreInfo(self):
        return self.restorePos, self.restoreSize


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.setWindowFlags(Qt.CustomizeWindowHint)  # 去掉标题栏

        self.title = TitleWidget()
        self.title.setFixedWidth(self.width())
        self.title.setFixedHeight(TITLE_HEIGHT)
        self.title.ButtonMin.clicked.connect(self.ButtonMinSlot)
        self.title.ButtonMax.clicked.connect(self.ButtonMaxSlot)
        self.title.ButtonRestore.clicked.connect(self.ButtonRestoreSlot)
        self.title.ButtonClose.clicked.connect(self.ButtonCloseSlot)

        self.ui.horizontalLayout.addWidget(self.title)

    # 最小化
    def ButtonMinSlot(self):
        self.showMinimized()

    # 最大化
    def ButtonMaxSlot(self):
        self.title.ButtonMax.setVisible(False)
        self.title.ButtonRestore.setVisible(True)
        self.title.saveRestoreInfo(self.pos(), QSize(self.width(), self.height()))
        desktopRect = QApplication.desktop().availableGeometry()
        FactRect = QRect(desktopRect.x() - 3, desktopRect.y() - 3, desktopRect.width() + 6,
                         desktopRect.height() + 6)
        self.setGeometry(FactRect)
        self.setFixedSize(desktopRect.width() + 6, desktopRect.height() + 6)

    # 恢复大小
    def ButtonRestoreSlot(self):
        # 最大化按钮显示
        self.title.ButtonMax.setVisible(True)
        # 隐藏恢复按钮
        self.title.ButtonRestore.setVisible(False)
        # 获取最大化之前的页面的大小数据
        windowPos, windowSize = self.title.getRestoreInfo()
        self.setGeometry(windowPos.x(), windowPos.y(), windowSize.width(), windowSize.height())
        self.setFixedSize(windowSize.width(), windowSize.height())

    # 关闭
    def ButtonCloseSlot(self):
        self.close()

    # 每次窗口有变化时刷新
    def paintEvent(self, event):
        # 设置标题宽度为当前窗体宽度
        self.title.setFixedWidth(self.width())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
