#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> get_pearvideo.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/29 14:46
@Desc    :
================================================="""
import requests
from lxml import etree
import re


headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}


def get_pearvideo_link_xpath():
    url = "https://www.pearvideo.com/category_8"
    html = requests.get(url, headers=headers).text
    datas = etree.HTML(html)
    video_links = datas.xpath('//*[@id="categoryList"]/li/div/a/@href')
    video_titles = datas.xpath('//*[@id="categoryList"]//div/a/div[2]/text()')

    for video_link, video_title in zip(video_links, video_titles):
        video_comple_link = "https://www.pearvideo.com/" + video_link
        print(video_title, video_comple_link)


def get_pearvideo():
    url = "https://www.pearvideo.com/category_8"
    html = requests.get(url, headers=headers).text
    # print(html)
    video_id = re.findall('<a href="(.*?)" class="vervideo-lilink actplay">', html)
    for i in video_id:
        new_url = "https://www.pearvideo.com/" + i
        data = requests.get(new_url, headers=headers).text
        playurl = re.findall(',srcUrl="(https://video.pearvideo.com/mp4/.*?.mp4)"', data)[0]
        print(playurl)
        content = requests.get(playurl, headers=headers)

        with open("./video/" + i + ".mp4", "wb") as f:
            f.write(content.content)
            print("下载 ", i, " 完毕")


def main():
    get_pearvideo()
    # get_pearvideo_link_xpath()


if __name__ == '__main__':
    main()
