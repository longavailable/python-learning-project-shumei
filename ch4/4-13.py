# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:48:56 2025

@author: 刘小龙
"""


str01 = '业精于勤荒于嬉'

list01 = list(str01)

print(str01, list01)

print('业' in str01, '业' in list01)
print('业精于' not in str01, '业精于' not in list01)

if '业' in str01:
    print('in')
else:
    print('NOT in')
