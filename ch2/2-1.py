# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 16:46:33 2025

@author: 刘小龙
"""

# 单行字符串

str1 = 'Hello, world!'

str2 = "Hello, world!"

print(str1 == str2)

str3 = "Liu's book"
print(str3)

str4 = '"Oh my god", says by Zhang'
print(str4)

# 多行字符串

str5 = '''古语
人有不为也，而后可以有为。
               ——《孟子》
'''
print(str5)

str6 = """古语
君子素其位而行，不愿乎其外。
               ——《中庸》
"""
print(str6)

# 续行符\

str7 = '古语\n \
    富贵不能淫，\n \
    贫贱不能移，\n \
    威武不能屈\n \
'
print(str7)