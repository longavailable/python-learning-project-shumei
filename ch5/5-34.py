# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:58:50 2026

@author: 刘小龙
"""

f = lambda x, y: x*y
print(f(3, 2))

list1 = [3, 2, -9, 8, -5, 7, 1]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list1.sort(key=lambda x: x**2)
print(list1)
# %%


# 映射函数map()
list1 = [3, 2, -9, 8, -5, 7, 1]
print(list1)
map1 = map(lambda x:x**2, list1)
print(type(map1))
print(list(map1))
list3 = []
for i in list1:
    list3.append(i**2)
print(list3)