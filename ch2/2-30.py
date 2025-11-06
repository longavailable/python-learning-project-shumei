# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 15:34:16 2025

@author: 刘小龙
"""

str1 = '学然后知不足，教然后知之困。知不足，然后能自反也；知困，然后能自强也'

str2 = "Knowledge advances by steps and not by leaps."

print(len(str1), str1.count('知'), str1.count('知', 0, 10))

print(len(str2), str2.count('o'), str2.count('o', 0, 10))

# 大小写转换

str1 = 'patience and application will carry us through.'

str2 = 'Put your shoulder to the wheel.'

str3 = "It's good to learn at another man's cost."

str4 = 'Step by step the ladderis ascended.'

str5 = 'Adversity leads to prosperity.'

print(str1.capitalize())

print(str2.lower())

print(str3.upper())

print(str4.swapcase())

print(str5.title())

# 搜索

str1 = '德不优者，不能怀远，才不大者，不能博见。'

print(str1.find('不'), str1.find('不', 5))
print(str1.find('不能'))

print(str1.find('不行'))
#print(str1.index('不行'))

print(str1.rfind('不'), str1.rindex('不能'))
