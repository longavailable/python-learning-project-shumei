# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 15:48:39 2025

@author: 刘小龙
"""

#cost = input('请输入消费金额：')
#cost = eval(input('请输入消费金额：'))
cost = float(input('请输入消费金额：'))

if cost < 100:
    print('消费金额小于100元，无折扣优惠')

    
x, y = eval(input('请输入两个数（逗号隔开）：'))

if x > y:
    x, y = y, x
print('排序结果：', x, y)

# float() vs eval()
#print(float(input('请输入两个数（逗号隔开）：')))

