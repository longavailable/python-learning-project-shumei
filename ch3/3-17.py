# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 15:33:35 2025

@author: 刘小龙
"""

from random import randint

sum = 0

while sum < 1000:
    
    tmp = randint(1, 100)
    
    sum += tmp
    
    if tmp > 90: 
        break
    
    #if tmp > 90: break
    
    print(tmp, end=' ')

else:
    print('恭喜您达成目标')
    
print(f'Sum is {sum}')

sum = 0
for i in range(100):
    
    print(i, end=' ')
    
    sum += i
    
    if sum > 50: break

print(f'Sum is {sum}')