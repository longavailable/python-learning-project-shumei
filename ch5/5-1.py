# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 15:34:00 2025

@author: 刘小龙
"""

# 无形参的函数
def func01():
    print('从此忧来非一事，岂容华发待流年')

a = func01()
print(a)
# %%

# 有形参/parameter的函数
def func02(a):
    b = a * 3 + 1
    return b

c = 5
print(func02(c))

d = func02(10)
print(d)

e = func02
print(e(20))
