# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu

Turtle star
"""

import turtle as t

t.speed(10) # 0-10之间

t.color('red', 'yellow')    # 画笔颜色、填充颜色

# star
t.begin_fill()

for _ in range(5):
    
    t.forward(150)
    t.right(144)
    #t.left(144)

t.end_fill()

t.clear()

# turtle star
# https://docs.python.org/3/_images/turtle-star.png
t.begin_fill()
tolerance = 1e-6
i = 0
while True:
    t.forward(200)
    t.left(170)
    
    current_position = t.position()
    if abs(current_position[0] - 0) < tolerance and abs(current_position[1] - 0) < tolerance:
        
        t.end_fill()
        
        print(i)
        break
    i += 1

t.hideturtle()

# 保存为ps/eps格式
#t.Screen().getcanvas().postscript(file='turtle-star.eps')
t.Screen().getcanvas().postscript(file='turtle-star.ps')

t.done()