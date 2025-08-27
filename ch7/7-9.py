# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

arr1 = np.ones(3)

print(arr1)
print(arr1.dtype)

arr2 = np.ones((2,3))

print(arr2)

arr3 = np.array(list('举世誉之而不加劝，举止非之而不加沮。')).reshape(2,9)

print(arr3)

arr4 = np.ones_like(arr3)

print(arr4)
print(arr4.dtype)