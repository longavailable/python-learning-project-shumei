# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

y = np.poly1d([1,-5,4])

print(y)

# 多项式求解
print(y([1,2,3]))

# 方程求解
print(y.roots)

print(np.roots(y))

z = np.poly1d([2,2,1,2])

print(z)

p = z + y

print(p)

# 微分/求导
print(p.deriv())

# 积分
print(p.integ())