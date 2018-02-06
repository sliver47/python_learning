#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/6 15:51
# @Author..: Rye
# @Site....: 
# @File....: guess.py
# @Software: PyCharm
age_of_oldboy = 56
guess = int(input("guess: "))
if guess == age_of_oldboy:
    print("yes,you got it.")
elif guess > age_of_oldboy:
    print("think smaller...")
else:
    print("think bigger...")
print(age_of_oldboy)
