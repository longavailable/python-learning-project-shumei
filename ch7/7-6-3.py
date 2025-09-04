# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

A = np.array([[3,2,1], [2,3,1], [1,2,3]], dtype=float)
b = np.array([39,34,26], dtype=float)

x = np.linalg.solve(A, b)   # 直接返回解向量
print(x)