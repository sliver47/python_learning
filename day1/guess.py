#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/6 15:51
# @Author..: Rye
# @Site....: 
# @File....: guess.py
# @Software: PyCharm

age_of_oldboy = 56

# 猜年龄——if else流程判断
"""
guess = int(input("guess: "))
if guess == age_of_oldboy:
    print("yes,you got it.")
elif guess > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger...")
print(age_of_oldboy)
"""
# 猜年龄——while循环
# while true方法——不能实现猜满3次就退出循环
"""
while True:
    guess = int(input("guess: "))
    if guess == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")
"""
# "while+条件"方法
count = 0
while count < 3:
    guess = int(input("guess: "))
    if guess == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1
else:
    print("you have tried too many times...fuck off")
# 加入了while条件 + else的方式——更加人性化
