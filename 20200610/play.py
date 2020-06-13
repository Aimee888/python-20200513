#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""=================================================
@Project -> File    : six-dialog_design -> play.py
@IDE     : PyCharm
@Author  : Aimee
@Date    : 2020/6/10 9:49
@Desc    :
================================================="""


def average_value(data_list):
    total = 0
    for data in data_list:
        total = total + data
    average_data = total / len(data_list)
    return average_data


def main():
    PercentC3Time_list = [94, 92, 86, 99, 92, 98, 93, 98]
    PercentIdleTime_list = [94, 92, 95, 99, 92, 98, 93, 98]
    average_a = int(average_value(PercentC3Time_list))
    print("PercentC3Time_list =", average_a)
    average_b = int(average_value(PercentIdleTime_list))
    print("PercentIdleTime_list =", average_b)


if __name__ == '__main__':
    main()


