# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 16:00:49 2025

@author: 刘小龙
"""

dict1 = {}

print(dict1, type(dict1))

dict2 = {'姓名':'张平', '年龄': 35, '性别':'男'}

print(dict2)

print(dict2['性别'])

# 字典的键(key)是唯一的
dict2 = {'姓名':'张平', '年龄': 35, '性别':'男', '姓名':'刘小龙'}

print(dict2)

# dict() 字典构造函数
dict3 = dict(姓名='张平', 年龄=35, 性别='男')
print(dict3)

# 修改
dict3['年龄'] = 38

print(dict3)
'''
dict3['职称'] = '教授'
print(dict3)
'''
print(dict3['年龄'])  # , dict3['职称'])

print(dict3.get('年龄'), dict3.get('职称'), dict3.get('职称', '其他'))

print(dict3)
print(dict3.pop('年龄'))  # 删除键值对，返回键对应的值
print(dict3)