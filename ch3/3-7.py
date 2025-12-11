# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 17:02:29 2025

@author: 刘小龙
"""

'''
x = float(input('请输入一个数字：'))

y = x if x > 10 else 10

print(y)
'''
def comparison(a, b=None):
    b = b if b else 5
    '''
    if b is not None:
        b = b
    else:
        b = 5
    '''
    print(a, b)
    print(max(a, b))

print(comparison(10))

print(comparison(3))

print(comparison(10, 8))

print(comparison(3, 8))