# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 15:37:59 2025

@author: 刘小龙
"""

a = 1
b = 2
print(a, b)

#c = a/b
#raise TypeError

try:
    print('定位1')
    c = a/b
    print('定位2')
except Exception as e:
    print('Exception:', e)
else:
    print('定位3')
finally:
    print('定位4')