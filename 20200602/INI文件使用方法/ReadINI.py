#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> ReadINI.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/2 14:35
@Desc    :参考链接：https://www.cnblogs.com/smart-zihan/p/11883699.html
================================================="""
import configparser

conf = configparser.ConfigParser()
conf.read("./test1.ini", encoding="utf-8")

sections = conf.sections()
print(sections)

options = conf.options('ITEMS')
print(options)

items = conf.items('ITEMS')
print(items)

value = conf.get('ITEMS', 'item1')
print(value)
