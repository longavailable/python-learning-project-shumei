# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 16:43:12 2025

@author: 刘小龙
"""

def func(a, b, c, d=800):
    print(a, b, c, d)

'''
func(3, 4, 5, 8)    # 位置匹配
func(d=3, a =4, b=8, c=9)   # 关键字参数key=value
func(3, b =10, d=8, c=9)
#func(b =10, d=8, c=9, 100)
'''
func(3, 4, 5)
func(6, 8, 10, 88)
print(func.__defaults__)

# b=[]# 空列表 / 初始化
def func02(a, b=[0]):
    b.append(a)
    #b = b + [a] # 生成一个新列表
    print(b)

func02(1)
func02(2)
func02(3)
func02(4, [5])
func02(10)

