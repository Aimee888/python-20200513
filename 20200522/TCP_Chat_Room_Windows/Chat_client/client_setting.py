#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> clent_setting.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 11:15
@Desc    :
================================================="""
import os
import shelve
from random import randint


HOST = "127.0.0.1"

# 缓冲区大小
BUFFERSIZE = 1024

# 服务端和客户端的连接地址
SOCK_PORT = 4444
SOCK_ADDR = HOST, SOCK_PORT

curuser = ''

client_port_list = []


# 客户端client.py文件中供pipe_server和pipe_client使用的套接字地址
# 因为每个客户端都必须有不同的套接字来作起到连接键盘输入和网络套接字之间的管道的作用
# 使用一个文件记录下每一次运行出现的端口号，以保证不重复
def get_client_pip_addr():
    if not os.path.exists("ports.dat"):
        f = shelve.open("ports")
        f["ports"] = []
    f = shelve.open("ports")
    while True:
        n = randint(4500, 10000)
        if n not in f["ports"]:
            f['ports'].append(n)
            break
    f.close()
    CLI_PIPE_PORT = n

    CLI_PIPE_ADDR = HOST, CLI_PIPE_PORT
    return CLI_PIPE_ADDR
