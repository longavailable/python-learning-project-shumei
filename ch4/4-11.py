# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:35:07 2025

@author: 刘小龙
"""

str01 = '业精于勤'
str02 = '荒于嬉'

# concatenate 拼接
str03 = str01 + str02

print(str03)

list01, list02 = list(str01), list(str02)

list03 = list01 + list02

print(list03)

print(id(list01), id(list02), id(list03))

str01 = '哈'

print(str01*100)

list01 = ['哈'] * 3
print(list01)
tuple01 = ('哈',) * 3
print(tuple01)

list03 = []*5
print(list03)