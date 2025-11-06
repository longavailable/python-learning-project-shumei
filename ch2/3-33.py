# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 16:26:36 2025

@author: 刘小龙
"""

# 字符串替换

str1 = "Hello, 张平。张平，你好"

print(str1.replace('张平', '数媒'))

# 比较测试

str1 = '苏A88888'

print(str1.startswith('苏A'), str1.startswith('浙A'))

print(str1.endswith('88'), str1.endswith('99'))

str2 = 'UsePython'

print(str1.isalpha(), str2.isalpha())

str3 = "13913688888"

str4 = "悟已往之不谏"
print(str1, str1.isalnum(), str2.isalnum(), str3.isalnum())

print(str4.isalpha(), str4.isupper(), str4.islower())

str5 = "13913688888"

str6 = "139136一二三四五"

str7 = '139136９９９９'

str8 = '139136ⅠⅡⅢⅣⅤ'

str9 = '3.1415'

print(str5.isdigit(), str5.isnumeric())
print(str6.isdigit(), str6.isnumeric())
print(str7.isdigit(), str7.isnumeric())
print(str8.isdigit(), str8.isnumeric())
print(str9.isdigit(), str9.isnumeric())
