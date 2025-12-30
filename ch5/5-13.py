# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 16:14:05 2025

@author: 刘小龙
"""

def func01(x):
    print('形参0', x, id(x))
    #x = x * 2 # 生成一个新列表
    x[0] = 77
    print('形参1', x, id(x))

'''
# 整型
y = 10
func01(y)
print(y, id(y))

# 字符串
s = 'test'
func01(s)
print(s)

# 元组
t = (10, 20)
func01(t)
print(t)
'''
l = list(range(5))
print(l, id(l))
l2 = l.copy()
print(l2, id(l2))
func01(l2)
print(l, id(l))

