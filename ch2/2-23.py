# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 16:37:34 2025

@author: 刘小龙
"""

# 类型自动转换

a = 8
b = 3.14
c = 2 + 2j

print(type(a), type(b), type(c))

x = a + b

print(x, type(x))

y = b + c

print(y, type(y))

z = a + c

print(z, type(z))

# 转换函数

a = 8.0

b = int(a)
print(a, b, type(a), type(b))

# 173   1E10
c = 1e10
print(type(c))

d = str(a)
print(a, type(a), d, type(d))

e = repr(a)
print(a, type(a), e, type(e))

str1 = 'Hello, Mr Zhang'
str2 = repr(str1)

print(str(str1), str2)
