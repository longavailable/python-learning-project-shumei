# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:32:45 2025

@author: 刘小龙
"""

a = 888

print(type(888), id(888), 888)

print(type(a), id(a), a)

a = 999

print(type(a), id(a), a)

print(type(888), id(888), 888)

help('keywords')

#help(True)


# keyword 模块

import keyword

print(keyword.kwlist)

print(keyword.iskeyword('Zhangpin'))

print(keyword.iskeyword('not'))

print(keyword.softkwlist)

print(keyword.issoftkeyword('Zhang'))

print(keyword.issoftkeyword('not'))

print(keyword.issoftkeyword('type'))