# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

np.random.seed(10)

arr1 = np.random.randint(0,10,size=8)
arr2 = np.random.randint(0,10,size=8)

print(arr1, arr2, sep='\n')

# 交集
print(np.intersect1d(arr1, arr2))

# 并集
print(np.union1d(arr1, arr2))

# 差集
print(np.setdiff1d(arr1, arr2))
print(np.setdiff1d(arr2, arr1))

# 异或
print(np.setxor1d(arr1, arr2))