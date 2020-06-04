#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> myUI_treewidget.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/3 8:51
@Desc    :QTreeWidget的基本样式方法
================================================="""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidgetItem
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtCore import Qt
from ui_treewidget import Ui_Form
from enum import Enum


# 节点类型的枚举类型
class TreeItemType(Enum):
    itGroupItem = 1001  # 群组
    itMemberItem = 1002  # 成员


class TreeColNum(Enum):  # 目录树的列号的枚举类型
    col_item_group = 0  # 组
    col_item_name = 1  # 姓名
    col_item_sex = 2   # 性别
    col_item_score = 3   # 分数
    col_item_excellent = 4   # 优秀


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数
        self.ui = Ui_Form()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI

        self.initial_tree()
        # 设置绑定事件
        self.ui.treeWidget.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self, qmodelindex):
        item = self.ui.treeWidget.currentItem()
        # 获取父节点
        parent = item.parent()
        index_row = -1
        if parent is None:
            # 获取当前节点的序号
            index_top = self.ui.treeWidget.indexOfTopLevelItem(item)
            print("当前在根节点Group" + str(index_top))
        else:
            # 获取父节点的序号
            index_top = self.ui.treeWidget.indexOfTopLevelItem(parent)
            print("当前在父节点Group" + str(index_top), end="")
            # 获取当前节点的序号
            index_row = parent.indexOfChild(item)
            print("下的" + str(index_row) + "号子节点", end="")

            # 打印当前行的内容
            print("Group=%s ,Name=%s, Sex=%s, Score=%s" % (item.text(0), item.text(1), item.text(2), item.text(3)))

    def initial_tree(self):
        # 设置表头
        self.ui.treeWidget.setHeaderLabels(['Group', 'Name', 'Sex', 'Score', 'Excellent'])
        # 设置表头背景色
        self.ui.treeWidget.setStyleSheet("QHeaderView::section{background:rgb(85, 181, 200);}")
        # 设置表头前景色
        brush = QBrush(QColor(255, 240, 0))
        brush.setStyle(Qt.SolidPattern)
        self.ui.treeWidget.headerItem().setForeground(0, brush)
        # 隐藏某一列
        self.ui.treeWidget.hideColumn(TreeColNum.col_item_excellent.value)
        # 设置列宽
        self.ui.treeWidget.setColumnWidth(1, 150)  # 第1列宽150

        # 假设QTreeWidget第一层的节点有10个
        for i in range(10):
            # 定义一个节点类型
            item = QTreeWidgetItem(TreeItemType.itGroupItem.value)
            # 设置节点的列对应的文本，此例为在group列写入数据group0,1,2,3...
            item.setText(TreeColNum.col_item_group.value, "Group" + str(i))
            # 设置根节点字体大小
            font = QFont()
            font.setPointSize(14)
            item.setFont(0, font)
            # 设置节点颜色
            brush = QBrush(QColor(210, 80, 234))
            brush.setStyle(Qt.SolidPattern)
            # 设置前景色
            item.setForeground(0, brush)
            # 设置背景色
            item.setBackground(1, brush)
            # 将节点添加进QTreeWidget
            self.ui.treeWidget.addTopLevelItem(item)

            # 假设QTreeWidget第二层的节点有3个
            for j in range(3):
                item_member = QTreeWidgetItem(TreeItemType.itMemberItem.value)
                item_member.setText(TreeColNum.col_item_group.value, str(j))
                item_member.setText(TreeColNum.col_item_name.value, "Alisa" + str(j))
                if j % 2 == 0:
                    item_member.setText(TreeColNum.col_item_sex.value, "girl")
                    item_member.setText(TreeColNum.col_item_score.value, "99")
                    item_member.setText(TreeColNum.col_item_excellent.value, "True")
                else:
                    item_member.setText(TreeColNum.col_item_sex.value, "boy")
                    item_member.setText(TreeColNum.col_item_score.value, "50")
                    item_member.setText(TreeColNum.col_item_excellent.value, "False")
                item.addChild(item_member)
                item.setExpanded(True)  # 设置节点展开
        font = QFont()
        font.setPointSize(14)
        self.ui.treeWidget.headerItem().setFont(0, font)

        # 第1个根节点的第二列设置为红色
        brush = QBrush(QColor(255, 0, 0))  # 红色
        brush.setStyle(Qt.SolidPattern)
        self.ui.treeWidget.topLevelItem(1).setBackground(2, brush)

        # 第0个根节点的的第1个子节点的第2列设置为黄色
        brush = QBrush(QColor(255, 255, 0))  # 黄色
        brush.setStyle(Qt.SolidPattern)
        self.ui.treeWidget.topLevelItem(0).child(1).setBackground(2, brush)

        # 设置右侧滚轮到指定位置
        child_item = self.ui.treeWidget.topLevelItem(5).child(2)
        self.ui.treeWidget.scrollToItem(child_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建app
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
