# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 16:27:48 2025

@author: 刘小龙
"""

'''
知识点回顾
for循环

for <expr>:
    block
[else:
     blcok
]

if 条件结构 二分支
if <expr>:
    blcok
else:
    block
'''

str1 = 'Live updates: Human remains found, search on for 2nd black box.'

for c in str1:
    if c.isdigit():
        print(f"{c} is a digit, that's end")
        break
    print(c, end="")
else:
    print('No digit.')  # no using break