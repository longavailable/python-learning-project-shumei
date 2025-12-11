# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 16:56:20 2025

@author: 刘小龙
"""

# python 内置函数

str01 = 'shumei'

list01 = list(str01)

# 序列长度
print(len(str01), len(list01))

print(max(str01), max(list01))

# min() 
print(min(str01), min(list01))

# enumerate() 

for i in str01:
    print(i)
    
for i in list01:
    print(i)

for i, k in enumerate(str01):
    print(i, k)
    
    str01[i] # 等价于 k

for i, k in enumerate(list01):
    print(i, k)

# sorted
print(str01, list01)
print(sorted(str01), sorted(list01))
print(sorted(str01, reverse=True), sorted(list01, reverse=True))

# reversed
str01 = 'shumei'
print(list(reversed(str01)))

# zip
str02 = 'jianyi'
print(list(zip(str01, str02)))

for i,j in list(zip(str01, str02)):
    print(i,j)

list01 = [None, False, 0]
print(all(list01), any(list01))

# del 关键字/keyword
# 1 删除对象本身
print(id(str01), str01)

del str01

#print(str01)

# 2 删除元素

list02 = list(str02)

print(id(list02), list02)

del list02[len(list02)-1]

print(id(list02), list02)

list04 = []
list03 = [None]*4
print(list03)
print(len(list04), len(list03))
































