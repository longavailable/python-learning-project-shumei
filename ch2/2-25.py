# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:37:44 2025

@author: 刘小龙
"""

a, b, c = 88.9999, 99.5555, 77.1234

print(max(a, b, c))

print(min(a, b, c))

print(sum([a, b, c]))

print(abs(b))

print(round(a, 2), round(b, 3), round(c, 0))

print(divmod(8, 5))

d = (8//5, 8%5)
print(d)

print(pow(2, 3), 2**3)

# int 类型 int() 函数
print(type(888))
print(int(888.9))
print(isinstance(888.9, int))

str1 = '5'; str11='10'
print(str1, type(str1))

str2 = repr(a+b)

print(str2, type(str2))

# 
str3 = eval(str1)

print(str3, type(str3))


str3 = "父母俱在，兄弟无故，一乐也"

print(len(str3))

# map
list1 = [1, 2, 3]
list2 = [3, 4, 1, 8]
list3 = [4, 3, 10]

list4 = list(map(max, [list1, list2, list3]))
print(list4)



