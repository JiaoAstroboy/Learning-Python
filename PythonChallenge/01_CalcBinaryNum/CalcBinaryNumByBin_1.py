#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/28 20:25
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNumByBin_1.py
# @Software :PyCharm


#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time     :2018/11/28 20:18
# @Author   :AstroBoy
# @Site     :
# @File     :CalcBinaryNumByCtype_2.py
# @Software :PyCharm

def CalcBinaryNumByBin(num):
    if (num >= 0):
        nbin = bin(num)
        return nbin.count('1')
    else:
        num = abs(num)
        nbin = bin(num - 1)
        return 32 - nbin.count('1')

print(CalcBinaryNumByBin(5))
print(CalcBinaryNumByBin(-1))