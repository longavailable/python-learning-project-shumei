# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

np.random.seed(10)

arr1 = np.random.randint(40,100,size=10)

c = arr1 < 60

print(c)

print(arr1[c])

print(arr1[(arr1>=60) & (arr1<=90)])

print(arr1[(arr1<60) | (arr1>90)])
