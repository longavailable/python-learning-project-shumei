# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:45:19 2025

@author: 刘小龙
"""
from pprint import pprint

str1 = "父母俱在，兄弟无故，一乐也"

print(len(str1))


list1 = [8, 10, 3, 5, 9]
#list1 = 'hello,shumei'

list_sorted = sorted(list1)

print(list1)

print(list_sorted)

list_sorted_re = sorted(list1, reverse=True)

print(list_sorted_re)

#print(help(list_sorted))

import math

print(math.pi)
'''
print(dir(math))
# dir()
# vars()    # __dict__属性，
# help()

pprint(vars(math))

print(help(math))
'''
# 四种取整运算
a, b = 2.6, -2.6
# 向上取整
print(math.ceil(a), math.ceil(b))
# 向下取整
print(math.floor(a), math.floor(b))
# 取整，向0取整
print(math.trunc(a), math.trunc(b))
# 四舍五入取整
print(round(a), round(b))

# 商和余数
a = 7
b = 3
# 运算符
print(a//b, a%b)
# 内置函数divmod()
print(divmod(a, b))
# math模块，取余
print(math.fmod(a, b))

# 取绝对值
a = 10.25; b = -10.85
# 内置函数abs()
print(abs(a), abs(b))
# math模块fabs()
print(math.fabs(a), math.fabs(b))

# 
angle = 30
arc_angle = math.radians(angle)
print(arc_angle, math.sin(arc_angle), math.cos(arc_angle))





