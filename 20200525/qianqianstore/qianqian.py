#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> qianqian.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/25 14:50
@Desc    :
================================================="""
import requests
from lxml import etree


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}


def main():
    # 访问斗破苍穹章节列表处的链接

    poix = {
        "http": "http://180.122.147.241:9999"
    }

    url = "https://www.qqxsnew.com/95/95631/"
    html = requests.get(url, headers=headers, proxies=poix).text
    datas = etree.HTML(html)
    chapter_titles_obj = datas.xpath('//*[@id="list"]/dl/dd[position()>12]')
    for chapter_title_obj in chapter_titles_obj:
        chapter_title_text = chapter_title_obj.xpath('./a/text()')[0]
        chapter_url = chapter_title_obj.xpath('./a/@href')[0]
        chapter_url = "https://www.qqxsnew.com" + chapter_url

        # 对每一章的链接发送请求
        html_chapter = requests.get(chapter_url, headers=headers).text
        datas_chapter = etree.HTML(html_chapter)
        content_chapter = datas_chapter.xpath('//*[@id="content"]/text()')
        for content_chapter_text in content_chapter:
            print(content_chapter_text)
            with open("斗破苍穹/" + chapter_title_text + ".txt", 'w', encoding='utf-8') as f:
                f.write(content_chapter_text)


if __name__ == '__main__':
    main()
