#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time....: 2018/2/5 16:47
# @Author..: Rye
# @Site....: 
# @File....: interaction.py
# @Software: PyCharm

# 简单交互程序
"""
username=input("username:")
password=input("password:")
print(username,password)
"""

# 高级交互程序——格式化输出

# 1-字符串拼接法——会开辟好几块内存，效率低下尽量不采用

name = input("name:")
age = int(input("age:"))
job = input("job:")
salary = input("salary:")

# 2-占位符法
info = '''
-------------- info of %s --------------
Name..: %s
Age...: %d
Job...: %s
Salary: %s
''' % (name, name, age, job, salary)

# 3-{}大括号法——官方推荐

# 3-1参数多的情况——思路清晰，官方推荐
info2 = '''
-------------- info of {_name} --------------
Name..: {_name}
Age...: {_age}
Job...: {_job}
Salary: {_salary}
''' .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

# 3-2参数少的情况
info3 = '''
-------------- info of {0} --------------
Name..: {0}
Age...: {1}
Job...: {2}
Salary: {3}
''' .format(name, age, job, salary)

# 打印结果
print(info3)