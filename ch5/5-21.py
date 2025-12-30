# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 15:41:52 2025

@author: 刘小龙
"""

a = [3, 4, 5]
print(a)
print(*a)

# %%
# 不定长参数
# 合成元组 *p
def func03(*p):
    #print(p)
    for i in p:
        i += 1
        print(i)

func03(1, 3, 8)
func03(888)

#%%

# 合成字典 **p
def func04(a, **p):
    """
    **p :: str
    'year':: int
    """
    print(a)
    for k, v in p.items():
        print(k + str(v))
    print(p['year'] + 5)

func04(1, x='python', key='javascript', year=2026)

