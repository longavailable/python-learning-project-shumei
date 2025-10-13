# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:32:14 2025

@author: 刘小龙
"""

a = 888
b = 999

# % 格式化
print('%10d%10d%10d' % (a, b, 1))
print('第一个数字：%10d第二个数字：%10d第三个数字：%10d' % (a, b, 1))

# str.format()
print('{},宁移白首之心，{},不坠青云之志'.format(a,b))
print('{:*>10d},宁移白首之心，{:*^10},不坠青云之志'.format(a,b))

# f-strings
r = float(input("请输入半径："))
print(f'圆半径为{r:*^10}，圆周率为{3.14:.5f}，圆面积为{3.14*r**2:08.1f}')

pi = 3.14

area = pi * r ** 2

print(f'圆半径为{r:*^10}，圆周率为{pi:.5f}，圆面积为{area:08.1f}')

str1 = F'圆半径为{r:*^10}，圆周率为{pi:.5f}，圆面积为{area:08.1f}'

print(str1)