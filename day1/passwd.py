#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/6 14:59
# @Author..: Rye
# @Site....: 
# @File....: passwd.py
# @Software: PyCharm
import getpass

_username = "Rye"
_password = "hcd"
username = input("username:")
password = getpass.getpass("password:")

if _username == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password!")

print(username, password)
