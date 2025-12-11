# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 15:54:30 2025

@author: 刘小龙
"""

str01 = '惠施多方，其书五车'

# seq(start: end: step) default 0, -1, 1

print(str01[:2], str01[:2:], str01[0:2], str01[0:2:1])

print(str01[7:], str01[7::], str01[7:9], str01[7:9:1], str01[-2:])

print(str01[1], str01[1:2])

print(str01, str01[:], str01[::])

# id()
print(id(str01), id(str01[:]), id(str01[::]), id(str01[:2:]), sep='\n')

# list()
# ★
list01 = list(str01)
print(list01, len(list01), id(list01))
list01[:2] = ['孔子', '孟子', '王阳明']
print(list01, len(list01),  id(list01))

# tuple()
tuple01 = tuple(str01)
tuple01[:2] = ['孔子', '孟子', '王阳明']