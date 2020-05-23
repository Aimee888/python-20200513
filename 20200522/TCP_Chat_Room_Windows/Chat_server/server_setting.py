#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> server_setting.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 10:46
@Desc    :
================================================="""
HOST = "127.0.0.1"

# 服务端和客户端的连接地址
SOCK_PORT = 4444
SOCK_ADDR = HOST, SOCK_PORT

# 服务端server.py文件中供pipe_server和pipe_client使用的套接字地址
SER_PIPE_PORT = 4321
SER_PIPE_ADDR = HOST, SER_PIPE_PORT

BUFFERSIZE = 1024
