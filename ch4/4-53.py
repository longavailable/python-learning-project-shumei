# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 15:36:18 2025

@author: 刘小龙
"""

import copy

str01 = '台阁生风'
list01 = list(str01)

str02 = '臼杵之交'
list02 = list(str02)

list03 = [list01, list02, 'zp']
print(id(list03), list03)

list04 = list03.copy()  # 浅复制
print(id(list04), list04)

list05 = copy.deepcopy(list03)  # 深复制
print(id(list05), list05)

list01[0] = 'zp'

list03[2] = 'lxl'
list04.append('zf')

print(list01, list03, list04, list05, sep='\n')


