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
# while true方法
"""
count = 0
while True:
    guess = int(input("guess: "))
    if count == 3:
        print("you have tried too many times...fuck off")
        break
    if guess == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1
"""
# "while条件 + else"方法——更加美观、人性化
"""
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
"""
# while循环优化——随便玩

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
    if count == 3:
        continue_confirm = input("Do you want to keep guessing?(exit with n) ")
        if continue_confirm != "n":
            count = 0
