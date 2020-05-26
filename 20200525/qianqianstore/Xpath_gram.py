#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> Xpath_gram.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/5/26 9:21
@Desc    :参考链接：https://www.cnblogs.com/xufengnian/p/10788195.html#_labelTop
================================================="""
# 1.选取节点
'''
/   如果是在最前面，代表从根节点选取，否则选择某节点下的某个节点.只查询子一辈的节点
    /html   查询到一个结果
    /div    查询到0个结果，因为根节点以下只有一个html子节点
    /html/body  查询到1个结果

//  查询所有子孙节点
    //head/script
    //div

.   选取当前节点

..  选取当前节点的父节点

@   选取属性
    //div[@id]  选择所有带有id属性的div元素
    <div id="sidebar" class="sidebar" data-lg-tj-track-code="index_navigation" data-lg-tj-track-type="1">

'''
# 2.谓语
'''
谓语是用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中。
//body/div[1]                body下的第一个div元素
//body/div[last()]           body下的最后一个div元素
//body/div[position()<3]     body下的位置小于3的元素
//div[@id]                   div下带id属性的元素
<div id="sidebar" class="sidebar" data-lg-tj-track-code="index_navigation" data-lg-tj-track-type="1">
//input[@id="serverTime"]    input下id="serverTime"的元素

模糊匹配
//div[contains(@class,'f1')] div的class属性带有f1的
通配符 *
//body/*                    body下面所有的元素
//div[@*]                   只要有用属性的div元素
//div[@id='footer']    //div  带有id='footer'属性的div下的所有div元素
//div[@class='job_bt'] //dd[@class='job-advantage']

运算符
//div[@class='job_detail'] and @id='job_tent'
//book/title | //book/price         选取 book 元素的所有 title 和 price 元素。
也可以百度搜索XPath语法

.//a/text()         当前标签下所有a标签的文字内容
//tr[position()>1 and position()<11] 位置大于1小于11
'''

# 需要注意的知识点
'''
1./和//的区别：/代表子节点，//代表子孙节点，//用的比较多
2.contains有时候某个属性中包含了多个值，那么使用contains函数
//div[contains(@class,'lg')]
3.谓语中的下标是从1开始的，不是从0开始的
'''
