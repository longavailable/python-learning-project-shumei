# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:05:39 2025

@author: 刘小龙
"""

from random import randint

sum = 0

while sum < 1000:
    tmp = randint(1, 100)
    #tmp = eval(input('请输入本次投入的零钱：'))
    sum += tmp #sum = sum + tmp
    print(tmp)

print(f'Sum is {sum}')

sum = 0
while True:
    tmp = randint(1, 100)
    print(tmp)
    sum += tmp
    if sum >= 1000: break

print(f'Sum is {sum}')