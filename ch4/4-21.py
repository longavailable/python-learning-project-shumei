# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 15:47:31 2025

@author: 刘小龙
"""

str0 = '激湍之下必有深潭，高丘之下必有浚谷'

list1 = list(str0)

print(list1.count('必'))

print(list1.count('必有'))

print(list1)

print(str0.count('必'))
print(str0.count('必有'))

# 弹出pop
print(list1.pop())
print(list1)

print(list1.pop(2))
print(list1)

# %%
str0 = '激湍之下必有深潭，高丘之下'

list1 = list(str0)
# 模拟堆栈
print(list1)
# 入栈
list1.append('必有浚谷')
print(list1)
# 出栈
list1.pop()
print(list1)
# 模拟队列
# 入队
list1.append('必有浚谷')
print(list1)
# 出队
list1.pop(0)
print(list1)

del list1[0]
print(list1)
