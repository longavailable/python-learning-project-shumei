# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 15:36:41 2025

@author: 刘小龙
"""

a = 1

print(a, type(a))

b = 1.414

print(b, type(b))

c = (2 + 1j)

print(c, type(c))

d = 0b1010
'''
0 + 2^1 + 0 + 2^3 = 10
'''

print(d, type(d))

print( 0b1010 + 8)

e = 0b110 
'''
0 + 2^1 + 2^2 = 6
'''

f = 0o12

print(f, type(f))

g = 0xA

print(g, type(g))

# bin(), oct(), hex(), int()

a = 10

b = bin(a)

print(b, type(b))

c = oct(a)

print(c, type(c))

d = hex(a)

print(d, type(d))

e = '1010'

f = int(e, 2)

print(f, type(f))

e = '12'

f = int(e, 8)

print(f, type(f))

e = 'A'

f = int(e, 16)

print(f, type(f))