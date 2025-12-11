# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:27:44 2025

@author: 刘小龙
"""

x = '博学之，审问之，慎思之，明辨之，笃行之。——《礼记.中庸》'

while x:
    print(x)
    x = x[:-6]
    if len(x) <= 10: break
else:
    print('end with no using break')

print('end')

x = '博学之，审问之，慎思之，明辨之，笃行之。——《礼记.中庸》'

while x:
    print(x)
    x = x[:-6]
else:
    print('end with no using break')

print('end')

x = '博学之，审问之，慎思之，明辨之，笃行之。——《礼记.中庸》'

while x:
    print(x)
    x = x[:-6]
    if len(x) > 100: break
else:
    print('end with no using break')

print('end')