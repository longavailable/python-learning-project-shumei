# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 16:51:46 2025

@author: 刘小龙
"""

list1 = ['怨不在大', '可畏惟人', '载舟覆舟', '所宜深慎']

list2 = ['张雪雁', "张平", "刘小龙"]

print('*'.join(list1))
print('*'.join(list2))

str1 = '-'.join(list1)
print(str1)

x = str1.split('-')

print(type(x), x, x == list1)

str1 = '寄蜉蝣于天地'

str2 = '渺沧海之一粟'

str3 = '哀吾生之须臾'

str4 = '羡长江之无穷'

print(str1.center(10, '*'))
print(str2.ljust(10, '*'))
print(str3.rjust(10, '*'))
print(str3.rjust(10))
print(str4.zfill(10))