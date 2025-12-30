# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 15:37:00 2025

@author: 刘小龙
"""

str01 = 'zhang'
print(str01)

tuple01 = tuple(str01)

print(tuple01)

#tuple01[0] = 'Z'

list01 = list(tuple01)

print(list01)

# 列表的操作和方法
list01[0] = 'Z'

list01.extend('Ping')

print(list01)

tuple01 = tuple(list01)
print(tuple01)

str01 = "*".join(list01)

print(str01)

# join/split

list02 = str01.split('*')
print(list02)


# sort() / sort(reverse=True)

list01.sort()

print(list01)

# sorted()