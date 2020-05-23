#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> server.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 10:07
@Desc    :参考链接：https://www.cnblogs.com/noonjuan/p/12063882.html
            需要设置的是server_setting.ini里面的内容，ip和port。
================================================="""
import shelve
from socket import *
from select import select
from multiprocessing import Process
# from server_setting import *
import threading
import inspect
import ctypes
import sys
import os
from random import randint
from ini_methods_set import get_value_ini


def listen(sock_server, pipe_server):
    # IO多路复用：循环监听套接字
    rlist = [sock_server, pipe_server]
    wlist = []
    xlist = []

    print("等待连接...")
    while True:
        rs, ws, xs = select(rlist, wlist, xlist)

        for r in rs:
            if r is sock_server:
                # 接受客户端连接
                conn, addr = sock_server.accept()
                rlist.append(conn)
            elif r is pipe_server:
                # 接收键盘输入并发送到所有客户端去
                conn, addr = pipe_server.accept()
                data = conn.recv(BUFFERSIZE)
                data = bytes("管理员：", "UTF-8") + data
                for c in rlist[2:]:
                    c.send(data)
                conn.close()
            else:
                # 接收客户端信息
                # 将客户端信息发送到所有的客户端中去
                try:
                    data = r.recv(BUFFERSIZE)
                except:
                    r.close()
                    rlist.remove(r)
                else:
                    print(data.decode(), end="")
                    for c in rlist[2:]:
                        c.send(data)


def clear_all():
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
    f = shelve.open("ports")
    f['ports'].clear()
    f.close()


# 关闭子线程
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


# 返回一个TCP服务端套接字
def server(addr):
    sock = socket(AF_INET, SOCK_STREAM, 0)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(10)
    return sock


# 返回一个TCP客户端套接字
def client(addr):
    sock = socket(AF_INET, SOCK_STREAM, 0)
    sock.connect(addr)
    return sock


if __name__ == '__main__':
    # # 首先将ports内容都删除
    # clear_all()

    # 创建两个套接字
    # 套接字sock_server是一个TCP服务端，负责服务端与客户端的交流
    # 套接字pipe_server也是一个TCP服务端，不过起到管道的作用，负责接收键盘输入
    ip, result_data = get_value_ini("server_setting.ini", "Server", "IP")
    port, result_data = get_value_ini("server_setting.ini", "Server", "PORT")
    port = int(port)
    pip_port, result_data = get_value_ini("server_setting.ini", "Server", "SER_PIPE_PORT")
    pip_port = int(pip_port)
    BUFFERSIZE, result_data = get_value_ini("server_setting.ini", "Server", "BUFFERSIZE")
    BUFFERSIZE = int(BUFFERSIZE)
    SOCK_ADDR = ip, port
    SER_PIPE_ADDR = ip, pip_port
    sock_server = server(SOCK_ADDR)
    pipe_server = server(SER_PIPE_ADDR)

    # # 开始一个子进程，执行listen函数
    # p = Process(target=listen, args=(sock_server, pipe_server))
    # p.daemon = True
    # p.start()

    # 开启一个子线程
    p = threading.Thread(target=listen, args=(sock_server, pipe_server))
    p.start()

    # 循环接收键盘输入
    while True:
        try:
            # 从标准输入流（键盘）读取一行
            data = sys.stdin.readline()
        except KeyboardInterrupt:
            # 如果遇到退出/中止信号，关闭套接字，结束子进程，退出程序
            sock_server.close()
            pipe_server.close()
            _async_raise(p.ident, SystemExit)
            # p.terminate()
            clear_all()
            break

        if not data:
            # 如果从键盘获取数据为空，继续循环
            continue
        else:
            # 获得键盘数据，创建客户端套接字pipe_client，将键盘输入传输给pipe_server
            pipe_client = client(SER_PIPE_ADDR)
            pipe_client.send(bytes(data, "UTF-8"))
            pipe_client.close()
