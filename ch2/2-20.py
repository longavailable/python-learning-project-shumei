# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 15:38:23 2025

@author: 刘小龙
"""

# 赋值运算符

# =

x, y = 2, 3
x += y  # 等价于 x = x + y
print(x, y)

x, y = 2, 3
x -= y  # 等价于 x = x - y
print(x, y)

x, y = 2, 3
x *= y  # 等价于 x = x * y
print(x, y)

x, y = 2, 3
x /= y  # 等价于 x = x / y
print(x, y)

x, y = 2, 3
x //= y  # 等价于 x = x //  y
print(x, y)

x, y = 2, 3
x %= y  # 等价于 x = x % y
print(x, y)

x, y = 2, 3
x **= y  # 等价于 x = x ** y
print(x, y)

x = 10  # 0000 1010
y = 7   # 0000 0111
print(bin(x), bin(y))

# 按位与 &：真（1）真为真，有假（0）为假

'''
   0000 1010
   0000 0111
&  0000 0010
'''
z = x & y

print(z, bin(z))

# 按位或 | ：有真（1）为真，假假（0）为假
'''
x  0000 1010
y  0000 0111
|  0000 1111
'''
z = x | y

print(z, bin(z))

# ~ >>  <<  
# 按位异或 ^ 真假为真，真真为假，假假为假

y = -3
print(y, bin(y))










