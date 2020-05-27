#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> create_two.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/27 13:44
@Desc    :
================================================="""
import qrcode
import os
from MyQR import myqr


def generate_simple():
    # 共40个尺寸，Version1是21*21, Version2是25*25。 公式：(V-1)*4 + 21
    qr = qrcode.QRCode(
        version=5,  # V = 5
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 纠错等级
        box_size=8,  # 二维码的像素点
    )

    # 二维码添加数据
    # qr.add_data("你是猪吗？")
    # qr.add_data("http://www.baidu.com")
    qr.add_data("我有点能理解你了！！！")

    # 生成二维码
    qr.make(fit=True)
    img = qr.make_image()
    # 保存二维码图片
    img.save("./image/img_data.png")
    img.show()


# myqr不支持中文
def generate_complex():
    myqr.run(
        words="I love you",
        version=5,
        level="H",
        picture="./image/dongman.jpg",
        colorized=True,  # True为彩色 False为黑白
        save_name="dongman.png",
        save_dir=os.getcwd() + "/image"
    )


def main():
    # 生成简单的二维码
    # generate_simple()
    generate_complex()


if __name__ == '__main__':
    main()
