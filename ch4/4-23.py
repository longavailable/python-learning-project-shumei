# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 16:56:57 2025

@author: 刘小龙
"""

str1 = '人有喜庆，不可生妒忌心，妒忌妒忌'
list1 = list(str1)
print(list1)
#list1.pop()
list1.remove('妒忌')
print(list1)

# %%

# reverse()

str1 = '人有祸患，不可生喜幸心'
list1 = list(str1)
print(list1)
list1.reverse()
print(list1)

# revesed()
str1 = '人有祸患，不可生喜幸心'
list1 = list(str1)
print(list1)
list2 = list(reversed(list1))
print(list2)