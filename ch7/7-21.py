# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np
np.random.seed(10)

x = np.arange(20)

y1 = 30*x + 20 + np.random.rand(20)

y1_fit = np.polyfit(x, y1, 1)

print(y1_fit)

y2 = 9*x**2 + 30*x + 10 + np.random.rand(20)

y2_fit = np.polyfit(x, y2, 2)

print(y2_fit)