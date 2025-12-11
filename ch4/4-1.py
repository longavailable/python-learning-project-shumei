# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 16:00:40 2025

@author: 刘小龙
"""

# 使用标记符合创建容器数据类型

# 列表list

list01 = [] # 空列表

print(list01, type(list01))

list02 = ['厉志贞亮', '悬梁刺股', '饮冰食檗']

list03 = [1, 48.8, '励志冰檗']  # 顶层类型是列表

print(list02, list03)

list04 = [[1,2,3], ['厉志贞亮', '饮冰食檗'], 1.1]

print(list04)

# 元组tuple ()

tuple01 = ()

tuple02 = ('厉志贞亮', '悬梁刺股', '饮冰食檗')

tuple03 = (1, 48.8, '励志冰檗')

print(tuple01, tuple02, tuple03, type(tuple01))

# 区别

print(list01, id(list01))
list01.append(8)
print(list01, id(list01))

print(tuple01, id(tuple01))
#tuple01.append(8)
print(tuple01, id(tuple01))

# %%
a = 3,4,5   # 等价于 a = (3, 4, 5)

print(a, type(a))