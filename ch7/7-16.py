# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

np.random.seed(10)

arr1 = np.random.randint(0,20,size=8).reshape(2,4)

print(arr1)

print(type(arr1))

# function within numpy module
print(np.max(arr1))

print(np.min(arr1), np.argmax(arr1), np.argmin(arr1), np.mean(arr1), np.median(arr1), sep='\n')

print(np.std(arr1), np.ptp(arr1), np.var(arr1), np.sum(arr1), np.prod(arr1), sep='\n')

print(np.cumsum(arr1), np.cumprod(arr1), sep='\n')

# methods with a numpy.ndarray object
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html

print(arr1.max(), arr1.min(), arr1.argmax(), arr1.argmin(), arr1.mean(), sep='\n')

print(arr1.std(), arr1.var(), arr1.sum(), arr1.prod(), sep='\n')

print(arr1.cumsum(), arr1.cumprod(), sep='\n')