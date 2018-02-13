#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/6 17:24
# @Author..: Rye
# @Site....: 
# @File....: while.py
# @Software: PyCharm

# while循环打印计数

"""
count = 0
while True:
    print("count: ", count)
    count = count + 1
    if count == 10
        break
"""

# 改写为for循环版本
# 下面句子range(10)中的10表在示0-9的范围内实现i循环10次
# 每循环一次加一
"""
for i in range(10):
    print("loop: ", i)
"""

# for循环跳跃打印

for i in range(0, 10, 2):
    print("loop: ", i)
