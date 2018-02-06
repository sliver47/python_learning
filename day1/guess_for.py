#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/6 18:04
# @Author..: Rye
# @Site....: 
# @File....: guess_for.py
# @Software: PyCharm

age_of_oldboy = 56

for i in range(3):
    guess = int(input("guess: "))
    if guess == age_of_oldboy:
        print("yes, you got it.")
        break
    elif guess > age_of_oldboy:
        print("think smaller...")
    else:
        print("think bigger...")
else:
    print("you have tried too many times...fuck off")
