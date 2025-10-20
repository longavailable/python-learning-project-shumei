# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 16:12:39 2025

@author: 刘小龙
"""

# 运算符优先级

a, b, c, d, e, f = 1, 2, 3, 4, 5, 6

print( not a > b and c + d or e == f)

print( ((not (a > b)) and (c + d)) or (e == f))

print( ((not (a > b)) and ((c + d)) or e) == f)