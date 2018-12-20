#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/28 20:46
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNumByBin_2.py
# @Software :PyCharm

def CalcBinaryNumByBin(num):
    nbin = bin(num & 0xffffffff)
    return nbin.count('1')

print(CalcBinaryNumByBin(5))
print(CalcBinaryNumByBin(-1))