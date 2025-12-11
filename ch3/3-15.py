# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:42:58 2025

@author: 刘小龙
"""

for c in '囊萤映雪':
    print(c, c, c)

n = eval(input('请输入数字x，以计算其阶乘：'))
fact = 1
# range(start, stop, step) 前闭后开区间[)
for i in range(1, n + 1):
    fact *= i # fact = fact * i

print(f'{n}的阶乘为{fact}')

n = eval(input('请输入数字x，以计算其阶乘：'))
fact = n
# range(start, stop, step) 前闭后开区间[)
for i in range(n-1, 1, -1):
    fact *= i # fact = fact * i

print(f'{n}的阶乘为{fact}')