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

# 按排序结果返回原序号
idx = np.argsort(arr1)

print(arr1, arr2, idx, sep='\n')

arr1.sort()

print(arr1)

