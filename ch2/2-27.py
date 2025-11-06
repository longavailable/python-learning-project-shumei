# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:38:10 2025

@author: 刘小龙
"""

import math

x = 2

print(math.sqrt(x))#, math.cbrt(x))

y = 3

# 幂函数、指数函数、对数函数

print(math.pow(x, y), x ** y, pow(x, y))

print(math.exp(y), math.e ** y)

print(math.log(1))

print(math.log(math.e))


print(math.log(2, 8))

print(math.log10(2), math.log(2, 10))

# 数论

x = 888888000; y = 240000000

print(math.gcd(x, y), math.lcm(x, y))

x = 4

print(math.factorial(x))

print(math.perm(6, 4))

print(math.comb(6, 4))
