#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> meizitu.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/3 14:44
@Desc    :
================================================="""
import requests
from lxml import etree


headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    'referer': "https://m.mzitu.com/"
}


def main():
    url = "https://www.mzitu.com/"
    html = requests.get(url, headers=headers)
    print(html)
    # datas = etree.HTML(html)
    # imgs_link = datas.xpath('//*[@id="pins"]/li/a/img/@src')
    # print(imgs_link)
    # for img_link in imgs_link:
    #     content = requests.get(img_link, headers=headers).content
    #     with open("pic/" + chapter_title_text + ".txt", 'a', encoding='utf-8') as f:
    #         f.write(content_chapter_text)


if __name__ == '__main__':
    main()
