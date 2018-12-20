#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/28 20:18
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNumByCtype_2.py
# @Software :PyCharm
from ctypes import *

def CalcBinaryNumByCtype(num):
    cnt = 0;
    while(c_int(num).value):
        cnt += 1
        num = num & (num -1)
    return cnt


print(CalcBinaryNumByCtype(5))
print(CalcBinaryNumByCtype(-1))