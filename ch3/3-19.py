# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 15:59:31 2025

@author: 刘小龙
"""

import random as rnd 

rnd.seed('LXL')

sum = 0

while sum < 1000:
    
    tmp = rnd.randint(1, 100)
    
    if tmp > 95: 
        break
    
    if tmp < 10:
        print('犒劳一下自己')
        continue
    
    sum += tmp
    
    print(tmp, end=' ')

else:
    print('恭喜您达成目标')
    
print(f'Sum is {sum}')


for i in range(100):
    pass