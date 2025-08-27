# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

np.random.seed(10)

arr1 = np.random.rand(2,4)

print('arr1:', arr1)

arr2 = np.random.randint(1,100,5)

print('arr2:', arr2)

arr3 = np.random.randint(1,100,(2,3))

print('arr3:', arr3)

arr4 = np.random.randn(2,3)

print('arr4:', arr4)