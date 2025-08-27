# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 10:02:47 2025

@author: 刘小龙
"""

import numpy as np

list1 = list(range(1000000))

arr1 = np.arange(1000000)

%time list2 = list1 * 2

%time list3 = [x*2 for x in list1]

%time arr2 = arr1 * 2