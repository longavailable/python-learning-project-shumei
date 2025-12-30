# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 16:30:02 2025

@author: 刘小龙
"""

# range()  前闭后开

a = range(20, 0, -5) #range(0, 21, 2)
print(a, type(a))

list01 = list(a)
print(list01)

for i in range(5):
    result = i**2
    print(result)

# %%

keys = ['name', 'age', 'city']
values = ['charlie', 35, 'Chicago']   

zip1 = zip(keys, values)
print(zip1, type(zip1))

dict01 = dict(zip1)
print(dict01)

print(list(zip1))

fruits = ['apple', 'banana', 'cherry', 'pineapple']
prices = [10, 8, 30]
stocks = [500, 800, 80000, 20, 200, 300]

zip2 = zip(fruits, prices, stocks)
#print(list(zip2))
for f, p, s in zip2:
    print(f, p, s)

# %%
import math
nums = list(range(5))
print(nums)
map1 = map(str, nums)
#map1 = map(math.sqrt, nums)
print(map1, type(map1))
# iterater(迭代器对象)， iterable(可迭代对象)
list01 = list(map1)
print(list01)

nums2 = list(range(10, 15))
list02 = list(map(lambda x1, x2: x1 + 1, nums, nums2))
print(list02)

