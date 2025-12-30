# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 16:45:05 2025

@author: 刘小龙
"""

set1 = {'荜门圭窦', '恶衣菲食', '食淡衣粗', '讳树数马'}

set2 = {'夺席谈经', '讳树数马', '项背相望', '荜门圭窦'}

set3 = set1.intersection(set2)
print(set3)

set4 = set1.union(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)
set6 = set2.difference(set1)
print(set6)

print(set1.issubset(set2), set1.issuperset(set2))

print(set3.issubset(set1))
print(set4.issuperset(set1))

set7 = set1 & set2
print(set7)
print(set7 == set3)