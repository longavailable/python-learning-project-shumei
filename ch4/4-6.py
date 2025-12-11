# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 15:34:04 2025

@author: 刘小龙
"""

str01 = '绳解木断；水滴石穿'
tuple01 = tuple(str01)
list01 = list(str01)

print(str01, tuple01, list01, sep='\n')

# 索引/indexing
# 正索引
print(str01[0], tuple01[0], list01[0], sep='\n')

print(str01[len(str01)-1], tuple01[-1], list01[-1], sep='\n')

for i in range(len(str01)):
    print(str01[i])

print(len(str01))

# 索引的范围
print(list01[5])

# list是可变的，字符串（str）、元组(tuple)是不可变的
print(id(list01))
# 修改
#str01[0] = '水'
list01[1] = '流'
#tuple01[2] = '林'

print(str01, tuple01, list01, sep='\n')
print(id(list01))