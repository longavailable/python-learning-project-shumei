# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:34:33 2025

@author: 刘小龙
"""

import math

a, b, c = 1, 2, 1

print(f'待求解的方程为:{a}x^2 + {b}x + {c} = 0')

delta = b**2 - 4 * a * c

x1 = (-b + delta**0.5)/2/a

x2 = (-b + math.sqrt(delta))/(2*a)

print(f'方程的解分别为：x1={x1}, x2={x2}')