# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 15:39:09 2025

@author: 刘小龙  2025888
"""

a = 5

b = 8

y = a + ｂ
print('和', y)

y = a - b

print('差', y)

y = a * b

print('乘积', y)

y = a / b
print('商', y)

y = a // b
print('取整', y)

y = a % b
print('取余', y)

y = a ** b

print('幂运算', y)

# 一元二次方程求根公式
# x = （-b +/- (b^2 - 4ac)^0.2)/2a

a = 4
b = 4
c = 1
if b**2 - 4 * a * c > 0:
    x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / ( 2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / ( 2 * a)
    print(x1, x2)
elif b**2 - 4 * a * c == 0:
    x1 = -b  / ( 2 * a)
    print(x1)
else:
    print('没有实数解！')

# 比较运算

a = 10
b = 20

print(a==b, a>b, a!=b, a<=b)

# 成员运算符 in / not in
str1 = "Life is short, use python"

str2 = 'py'
if str2 in str1:
    print('W在里面')
else:
    print('W不在')    
# not in 本身是一个成员运算符
if str2 not in str1:
    print('不在里面')
else:
    print('在里面')  
# in是一个成员运算符，not逻辑运算符
if not str2 in str1:
    print('不在里面')
else:
    print('在里面')  

# 标识号比较运算 is / not is
# id()

str1 = [3, 6]
print(id(str1), str1)

str2 = str1
print(id(str2), str2)

str3 = str1.copy()
print(id(str3), str3)

if str2 is str1:
    print("我们一样滴")
else:
    print("我们不一样")

if str3 is str1:
    print("我们一样滴")
else:
    print("我们不一样")

if str3 == str1:
    print("我们是相等的")
else:
    print("我们不相等")

# 逻辑运算符 and or not
# and 真真为真，有假为假
# or  有真为真，假假为假
print("--------------------------")
a = 50
b = 40
c = 30
if b > a and b < c:
    print("b在ac中间")
else:
    print("不在ac间")

print("--------------------------")
a = 10
b = 20
c = 30
if b > a or b < c:
    print("==============")
else:
    print("不在ac间")

if not a > b: print("a > b")
































