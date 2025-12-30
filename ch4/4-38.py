# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 16:35:15 2025

@author: 刘小龙
"""

dict1 = dict(姓名='张平', 年龄=35, 性别='男')

print(dict1)

#print(list(dict1.keys()))

#print(dict1.values(), dict1.items())

#for k, v in list(dict1.items()): # 与下一行等价
for k, v in dict1.items():
    print(k, v)
    '''
    具体操作
    '''

for k in dict1:
    print(k, dict1[k])
    
# update(d)

dict2 = {'姓名': '刘小龙', '专业': '数媒'}

dict1.update(dict2)

print(dict1)

'''
# dict[key] = value
只能修改/更新一个键值对
'''

del dict1['姓名']
# del dict1
print(dict1)

print(len(dict1))

if '姓名' in dict1:
    dict1['姓名'] = '张平'

print(dict1)

# clear()
dict1.clear()
print(dict1)
