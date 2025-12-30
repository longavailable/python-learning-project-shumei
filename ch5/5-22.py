# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 16:01:55 2025

@author: 刘小龙
"""

# *可迭代对象的解包运算符
# **字典键值对的解包运算符

yyy= 888

def func01(x, y, z):
    print(x, y, z)
    print(x+y+z)
    xxx = 1000
    global yyy 
    yyy = 999
    print(xxx + yyy)

# 列表，集合，元组
a = [1, 2, 3]
print(func01(*a))

# 字典
b = {'r':1, 's':2, 't': 3}
print(func01(*b))
print(func01(*b.keys()))    # list
print(func01(*b.values()))  #list

# 字典的键必须与函数的形参名称一致
b = {'z':1, 'x':2, 'y': 3}
print(func01(**b))      # key=value

print(yyy)
print(xxx)