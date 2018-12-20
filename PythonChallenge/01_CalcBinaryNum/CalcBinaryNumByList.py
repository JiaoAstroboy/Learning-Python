#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/28 21:04
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNumByList.py
# @Software :PyCharm

counts = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

def CalcBinaryNumByList(num):
    result = 0
    for i in range(0,32,4):
        result += counts[(num >> i) & 0xf]

    return result

print(CalcBinaryNumByList(5))
print(CalcBinaryNumByList(-1))