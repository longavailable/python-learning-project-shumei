# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 16:03:26 2025

@author: 刘小龙
"""

def func(n):
    if n == 1:
        return 1
    else:
        #print(n)
        return n * func(n-1)

#print(func(2001))

fact = 1
n = 5
for i in range(1, n+1):
    fact *= i

print(fact)