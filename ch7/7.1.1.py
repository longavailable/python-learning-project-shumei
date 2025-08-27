# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

# list.append
list0 = [1,2,3]

print(id(list0), list0)

list0.append(5)

print(id(list0), list0)

# numpy.append
arr_1d = np.array([1, 2, 3])

print(id(arr_1d), arr_1d)

arr_1d_new = np.append(arr_1d,5)

print(id(arr_1d), arr_1d)

print(id(arr_1d_new), arr_1d_new)