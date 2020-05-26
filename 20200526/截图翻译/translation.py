#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> translation.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/26 18:10
@Desc    :  1. 清空剪切板
            2. 监测键盘按键"ctrl_alt+a", 阻塞程序直到得到截图
            3. 将图片中的文字提取出来，用的是百度云的api
            4. 翻译文字，用的是网页上在线翻译的接口：http://fy.iciba.com/
================================================="""
import requests
from ctypes import windll, c_int
from PIL import ImageGrab
import keyboard
import time
from aip_baidu_img2text_recognition import get_text_from_image
from pprint import pprint


# 清空剪切板
def clear_clipboard():
    # ============== 清空剪切板, c_int(0)内存中的存储区域
    user32 = windll.user32
    # 打开剪切板
    user32.OpenClipboard(c_int(0))
    # 清空剪切板
    user32.EmptyClipboard()
    # 关闭剪切板
    user32.CloseClipboard()


# 获取截图
def get_image(img_path):
    # 获取图片内容
    while True:
        image = ImageGrab.grabclipboard()
        if image:
            image.save(img_path)
            break
        else:
            time.sleep(2)


# 翻译文本
def translation(word):
    result = requests.post(
        url="http://fy.iciba.com/ajax.php?a=fy",
        data={"f": "auto", "t": "auto", "w": word}
    ).json()
    return result


def main():
    # 清空剪切板
    clear_clipboard()

    # 检测键盘按下，没检测到按下截图键，继续等待，检测到了，代码往下走。此处有个阻塞
    keyboard.wait(hotkey="ctrl+alt+a")

    # 得到截屏的图片存放到剪切板
    get_image("screen.png")

    print("开始识别！")

    # 获取图片中的文字
    word = get_text_from_image("screen.png")

    # 翻译文字
    result = translation(word)
    # pprint(result)
    # 中文转英文
    print(result["content"]["out"])
    # 英文转中文
    # print(result["content"]["word_mean"])


if __name__ == '__main__':
    main()
