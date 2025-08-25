# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:22:40 2025

@author: Xiaolong Liu

思考：如何确定循环次数
"""

import turtle as t

t.speed(10)

t.color('red', 'yellow')

t.begin_fill()


# 方法1 forloop
tolerance = 1e-6
for i in range(700):
    
    t.forward(100)
    t.left(70)
    
    current_position = t.position()
    if abs(current_position[0] - 0) < tolerance and abs(current_position[1] - 0) < tolerance:
        
        t.end_fill()

        t.clear()
        print(i)
        break

# 方法2 while loop
t.begin_fill()
i = 0
while True:
    t.forward(100)
    t.left(70)
    
    current_position = t.position()
    if abs(current_position[0] - 0) < tolerance and abs(current_position[1] - 0) < tolerance:
        
        t.end_fill()
        print(i)
        break
    i += 1
  
t.done()