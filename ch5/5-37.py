# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 16:12:17 2026

@author: 刘小龙
"""

def g():
    a = 1
    while True:
        yield a
        a = a + 1

c = g()
for i in range(10):
    print(next(c), end=' ')

print()
c = g()
for i in c:
    if i >= 15: break
    print(i, end=' ')

print(next(c))

c = g()
for i in range(20):
    print(c.__next__(), end=' ')

print(c.__next__())