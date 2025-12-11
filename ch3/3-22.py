# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 16:43:41 2025

@author: 刘小龙
"""

# for 循环
for i in range(1, 10): # range() 前闭后开区间 range(1,10,1)
    for j in range(1, i+1):
        print( f'{j}*{i}={i*j:>2}', end="  ")
    print()

# while 循环
i = 9
while i > 0:
    j = 1
    while j < i+1:
        print( f'{j}*{i}={i*j:>2}', end="  ")
        j += 1
    i -= 1
    print()

# for + while
for i in range(1, 10):
    j = 1
    while j < i+1:
        print( f'{j}*{i}={i*j:>2}', end="  ")
        j += 1
    print()
    