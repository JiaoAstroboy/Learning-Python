#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/26 21:27
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNum_Ctype.py
# @Software :PyCharm

from ctypes import *
def CalcBinaryNumByCtype(num):
    count = 0
    flag = 1
    while(c_int(flag).value):
        if (c_int(flag & num).value):
            count += 1
        flag = flag << 1
    return count


print(CalcBinaryNumByCtype(5))
print(CalcBinaryNumByCtype(-1))

