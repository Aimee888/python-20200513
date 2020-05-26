#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> aip_baidu_img2text_recognition.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/26 18:44
@Desc    :借用api：https://blog.csdn.net/qq_33333654/article/details/102723118
            文字识别接口说明：https://ai.baidu.com/ai-doc/OCR/Dk3h7yf8m
================================================="""
from aip import AipOcr


"""你的 APPID AK SK"""
APP_ID = "17593750"
API_KEY = "VExogNuAiDslahMNe2uRn5IB"
SECRET_KEY = "zILi6zsRwgKa1dTmbv2Rw8uG1oPGyI9A"

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_text_from_image(image_path):
    if isinstance(image_path, bytes):
        image = image_path
    else:
        with open(image_path, "rb") as f:
            image = f.read()
    result_data = client.basicAccurate(image)
    # print(result_data)
    result_str = ""
    if result_data["words_result"]:
        for data in result_data["words_result"]:
            result_str += data['words']
    else:
        result_str = "No content"
    return result_str

