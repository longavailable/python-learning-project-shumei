# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:54:04 2025

@author: 刘小龙
"""

# set()

# 空集合
set1 = set()

dict1 = {}
print(type(dict1))

set2 = {'清风劲节', '尧年舜日'}

str1 = '清风劲节'
# set(), list(), tuple()
# 参数均为可迭代对象。str, list, tuple, dictionary
set3 = set(str1)

print(set1, type(set1))
print(set2, set3)