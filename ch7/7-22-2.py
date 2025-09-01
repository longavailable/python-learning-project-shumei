# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np
np.random.seed(10)

arr1 = np.random.randint(1, 20, size=10)

# 排序
arr2 = np.sort(arr1)

print(arr1, arr2, sep='\n')

# 方法1 利用argsort
arr3 = arr1[np.argsort(-arr1)]

# 方法2 利用切片slicing
arr4 = arr2[::-1]

# 方法3 利用内置sorted函数
arr5 = np.array(sorted(arr1, reverse=True))

print(arr3, arr4, arr5, sep='\n')