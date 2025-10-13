# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 16:28:39 2025

@author: 刘小龙
"""

x, y = True, False

print(x, type(x))

print(y, type(y))

x = 3 < 4

print(x, type(x))

y = 3 == 4

print(y, type(y))

a = True + 9

print(a, type(a))

b = False + 9

print(b, type(b))

# isinstance()

print(isinstance(True, int))
print(isinstance(1, int))
print(isinstance(1.414, int))