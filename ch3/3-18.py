# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 15:43:42 2025

@author: 刘小龙
"""

import random as rnd

#rnd.seed(8888) #重现结果

sum = 0

for i in range(100):
    
    #print(i)
    
    score = rnd.normalvariate(80, 20)
    
    score = round(score)
    
    if score < 60:
        print(score, end=' ')
        continue