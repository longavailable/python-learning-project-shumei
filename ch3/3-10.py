# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 16:44:13 2025

@author: 刘小龙
"""

a, b, c = eval(input('请输入a,b,c的值（逗号隔开）：'))

print(f'待求解的方程为:{a}x^2 + {b}x + {c} = 0')

delta = b**2 - 4 * a * c
x1 = (-b + delta**0.5)/2/a

x2 = (-b - delta**0.5)/(2*a)

if delta > 0:
    print(f'方程的解分别为：x1={x1}, x2={x2}')
elif delta == 0:
    print(f'方程的解分别为：x1=x2={x1}')
else:
    print(f'方程无实数解：x1={x1}, x2={x2}')