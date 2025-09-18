# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 16:50:22 2025

@author: 刘小龙,20258888
"""

i = 1

while i <= 9:
    j = 1
    while j <=i:
        print('%d*%d=%2d' % (j, i, i*j), end='\t')
        j+=1
    print()
    i+=1

