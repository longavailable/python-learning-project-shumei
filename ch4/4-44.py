# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 16:01:14 2025

@author: 刘小龙
"""

set1 = {'策名就列', '端本正源', '骥子龙文'}

print(len(set1), set1)

for x in set1:
    print(x)

for i, j in enumerate(set1):
    print(i, j)

list1 = list(set1)
print(list1[0], list1[-1])

print(set1)
set1.remove('策名就列')
print(set1)
set1.discard('骥子龙文')
print(set1)
#set1.remove('策名就列')
#print(set1)
set1.discard('骥子龙文')
print(set1)

set1.add('公而忘私')
print(set1)

# 弹出pop()
str1 = set1.pop()
print(str1)
print(set1)

# update()
set1.update({'公而忘私'})
print(set1)
set1.update({'公而忘私', '国而忘家'})
print(set1)

str1= '1234567898754'
list1 = list(str1)
print(list1)
set3 = set(str1)
print(set3)
list1 = list(set3)
print(list1)

# clear()
set3.clear()
print(set3)

# del
del set3
#print(set3)








