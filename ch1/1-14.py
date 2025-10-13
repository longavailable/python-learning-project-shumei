# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 15:54:31 2025

@author: 刘小龙
"""

age = input('请输入您的年龄：')

print(age, type(age))
#print(age + 10)

age2 = int(age)

print(age2, type(age2))
print(age2 + 10)

age3 = eval(age)    # eval()  evaluate

print(age3, type(age3))

print(age3 + 20)

age = eval(input('请输入您的年龄：'))
print(age, type(age))

name = input('请输入您的姓名：')
print(name, type(name))