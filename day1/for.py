#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/11 17:59
# @Author..: Rye
# @Site....: 
# @File....: for.py
# @Software: PyCharm

# continue：跳出本次循环，进入到下次循环
#   break ：结束整个循环

for i in range(0, 10):
    if i < 5:
        print("loop", i)
    else:
        continue
    print("hehe...")
