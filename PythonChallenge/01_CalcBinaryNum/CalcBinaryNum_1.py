#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/23 21:48
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNum_1.py
# @Software :PyCharm

def CalcBinaryNum(num):
    cnt = 0;
    while(num):
        if (num & 1):
            cnt += 1
        num = num >> 1
    return cnt

print(CalcBinaryNum(-1))
