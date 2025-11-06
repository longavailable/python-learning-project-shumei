# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 16:05:09 2025

@author: 刘小龙
"""

# random 模块

import random

#random.seed(888)

print(random.uniform(0, 1))

print(random.randint(1, 20))

print(random.randrange(0, 50, 5))

print(random.choice((1,2,3.2, 5, 88, "你好")))

import random as rnd

print(rnd.uniform(0, 1))

from random import uniform

print(uniform(0, 1))

from random import uniform as uf

print(uf(0, 1))
