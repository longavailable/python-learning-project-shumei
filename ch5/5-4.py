# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 15:46:29 2025

@author: 刘小龙
"""

def num_add(a, b):
    return a+b

print(num_add(3,5))

c, d = 3, 4
print(num_add(c, d))

# 不指定返回值
def func():
    print('天行健君子以自强不息')
    return

e = func()
print(e)

# 多个返回值
def add(a, b):
    c = a + b
    return a, b, c

e, f, g = add(8, 18)

print(e, f, g)
h = add(8, 18)[-1]
print(h)

# 多个return
def func(a,b):
    if a < b:
        return b
    elif a > b:
        return a
    else:
        return 888
    
print(func(105,105))