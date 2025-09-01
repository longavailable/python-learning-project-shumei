# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

arr1 = np.array([1,3,5,7])

arr2 = np.append(arr1, [2,4])

arr3 = np.insert(arr1, 2, 4)

arr4 = np.delete(arr1, [0,2])

print(arr1, arr2, arr3, arr4, sep='\n')
