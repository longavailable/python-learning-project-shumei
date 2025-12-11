# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 16:32:35 2025

@author: 刘小龙
"""

# append
list01 = list('唯天下之静者')
print(list01, id(list01), len(list01))

list01.append('乃能见微而知著')

print(list01, id(list01), len(list01))
'''
list01 = list('唯天下之静者')
print(list01, id(list01), len(list01))
list03 = list01 + ['乃能见微而知著']
print(list03, id(list03))
'''
# extend

list01 = list('唯天下之静者')
print(list01, id(list01), len(list01))
list01.extend('乃能见微而知著')
print(list01, id(list01), len(list01))

# 序列加法

list01 = list('唯天下之静者')
print(list01, id(list01), len(list01))

list03 = list01 + list('乃能见微而知著')

print(list03, id(list03), len(list03))
print(list01, id(list01), len(list01))

# insert
list01 = list('唯天之静者')
print(list01, id(list01), len(list01))
list01.insert(2,'下')
print(list01, id(list01), len(list01))

# count
str01 = 'Hello world'
print(str01.count('o'))
print(str01.count('ll'))

list01 = list(str01)
print(list01, id(list01), len(list01))
print(list01.count('l'))
print(list01.count('ll'))

# indexing
print(str01[0])
print(str01.index('l'))

print(list01[4])
print(list01.index('l'))
print(list01.index('ll'))

















