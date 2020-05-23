#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> client.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/23 10:08
@Desc    :参考链接：https://www.cnblogs.com/noonjuan/p/12063882.html
            需要设置的是client_setting.ini里面的内容，ip和port。
================================================="""
import sys
from socket import *
from select import select
import threading
import inspect
import ctypes
from ini_methods_set import get_value_ini


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


def connect(sock_client, pipe_server, name):
    # IO多路复用：循环监听套接字
    rlist = [sock_client, pipe_server]
    wlist = []
    xlist = []

    while True:
        rs, ws, xs = select(rlist, wlist, xlist)

        for r in rs:
            if r is sock_client:
                # 接受服务端的信息
                data = sock_client.recv(BUFFERSIZE).decode()
                print(data, end="")
            elif r is pipe_server:
                # 接受键盘输入并发送给服务端
                conn, addr = pipe_server.accept()
                data = conn.recv(BUFFERSIZE)
                data = bytes(name + "：", "UTF-8") + data
                sock_client.send(data)
                conn.close()


def get_name():
    return input("User name: ")


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


if __name__ == '__main__':
    # 使用get_name函数获得用户名
    name, result_data = get_value_ini("client_setting.ini", "Client", "CLIENT_NAME")
    server_ip, result_data = get_value_ini("client_setting.ini", "Client", "SERVER_IP")
    server_port, result_data = get_value_ini("client_setting.ini", "Client", "SERVER_PORT")
    server_port = int(server_port)
    SOCK_ADDR = server_ip, server_port

    # 创建两个套接字
    # 套接字sock_client是一个TCP客户端，负责服务端与客户端的交流
    # 套接字pipe_server也是一个TCP服务端，不过起到管道的作用，负责接收键盘输入
    sock_client = client(SOCK_ADDR)
    sock_client.send(bytes(name + "加入了聊天室。\n", "UTF-8"))
    client_ip, result_data = get_value_ini("client_setting.ini", "Client", "CLIENT_IP")
    CLI_PIPE_PORT, result_data = get_value_ini("client_setting.ini", "Client", "CLI_PIPE_PORT")
    CLI_PIPE_PORT = int(CLI_PIPE_PORT)
    CLI_PIPE_ADDR = client_ip, CLI_PIPE_PORT
    BUFFERSIZE, result_data = get_value_ini("client_setting.ini", "Client", "BUFFERSIZE")
    BUFFERSIZE = int(BUFFERSIZE)
    pipe_server = server(CLI_PIPE_ADDR)

    # # 开始一个子进程，执行connect函数
    # p = Process(target=connect, args=(sock_client, pipe_server, name))
    # p.daemon = True
    # p.start()

    # 开启一个子线程
    p = threading.Thread(target=connect, args=(sock_client, pipe_server, name))
    p.start()

    # 循环接收键盘输入
    while True:
        try:
            # 从标准输入流（键盘）读取一行
            data = sys.stdin.readline()

            if not data:
                # 如果从键盘获取数据为空，继续循环
                continue
            else:
                # 获得键盘数据，创建客户端套接字pipe_client，将键盘输入传输给pipe_server
                pipe_client = client(CLI_PIPE_ADDR)
                pipe_client.send(bytes(data, "UTF-8"))
                pipe_client.close()

        except:  # KeyboardInterrupt:
            # 如果遇到退出/中止信号，发送退出信息，关闭套接字，结束子进程，退出程序
            sock_client.send(bytes(name + "退出了聊天室。\n", "UTF-8"))
            sock_client.close()
            pipe_server.close()
            _async_raise(p.ident, SystemExit)
            # p.terminate()
            break
