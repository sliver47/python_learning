#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/11 17:59
# @Author..: Rye
# @Site....: 
# @File....: for.py
# @Software: PyCharm

# continue：跳出本次循环，进入到下次循环
#   break ：结束整个循环

# continue例子：
"""
for i in range(0, 10):
    if i < 3:
        print("loop", i)
    else:
        continue
    print("hehe...")
"""

# break例子：大循环与小循环的嵌套

for i in range(10):
    print("-----------", i)
    for j in range(10):
        print(j)
        if j > 5:
            break
