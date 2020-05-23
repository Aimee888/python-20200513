#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : FDS -> ini_methods_set.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/4/28 17:09
@Desc    :Ini 的处理集合
@Version : 0.0.0.1 --> 2020/4/28 --> 第一次重构代码
================================================="""

import configparser
import os


class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


def is_ini_exist(ini_path):
    ini_exist = os.path.exists(ini_path)
    if not ini_exist:
        return False
    return True


def is_section_exist(ini_path, section):
    conf = MyConfigParser()
    conf.read(ini_path)
    sections = conf.sections()
    section_exist = False
    for section_data in sections:
        if section_data == section:
            section_exist = True
    return section_exist


def is_key_exist(ini_path, sec_name, key_name):
    conf = MyConfigParser()
    conf.read(ini_path)
    options = conf.options(sec_name)
    key_exist = False
    for option in options:
        if option.lower() == key_name.lower():
            key_exist = True
    return key_exist


def get_sections(ini_path):
    conf = MyConfigParser()
    conf.read(ini_path)
    sections = conf.sections()
    return sections


def get_keys(ini_path, sec_name):
    conf = MyConfigParser()
    conf.read(ini_path)
    options = conf.options(sec_name)
    return options


def get_value(ini_path, sec_name, key_name):
    conf = MyConfigParser()
    conf.read(ini_path)
    value = conf.get(sec_name, key_name)
    return value


def get_key_value_dic(ini_path, sec_name):
    conf = MyConfigParser()
    conf.read(ini_path)
    items = conf.items(sec_name)
    print(items)


# 知道ini文件路径，section, key，得到value的值
def get_value_ini(status, section_status_ini, key_status_ini):
    result_data = 0
    value_status_ini = ""
    if not is_ini_exist(status):  # 不存在status.ini
        print("ERROR!!!%s is not exsit" % status)
        result_data = 1
        return value_status_ini, result_data
    else:
        if not is_section_exist(status, section_status_ini):  # 不存在[Status]
            print("ERROR!!!%s is not exsit section %s" % (status, section_status_ini))
            result_data = 1
            return value_status_ini, result_data
        else:
            if not is_key_exist(status, section_status_ini, key_status_ini):  # [Status]下不存在stage=
                print("ERROR!!!%s's section %s is not exsit key %s" %
                          (status, section_status_ini, key_status_ini))
                result_data = 1
                return value_status_ini, result_data
            else:
                value_status_ini = get_value(status, section_status_ini, key_status_ini)
    return value_status_ini, result_data


def add_section(ini_path, sec_name):
    conf = MyConfigParser()
    conf.add_section(sec_name)
    conf.write(open(ini_path, "a"))


def set_key_value(ini_path, sec_name, key_name, value_name):
    conf = MyConfigParser()
    conf.read(ini_path)
    conf.set(sec_name, key_name, value_name)
    conf.write(open(ini_path, "w"))

