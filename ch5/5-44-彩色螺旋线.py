# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:53:33 2026

@author: 刘小龙
"""

import turtle

turtle.speed(6)

turtle.color('red', 'yellow')

turtle.begin_fill()

for _ in range(40):
    turtle.fd(100)
    turtle.right(70)

turtle.end_fill()

turtle.done()

# %%

import turtle
#turtle.speed(10)
turtle.pensize(2)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'purple', 'blue', 'orange']
turtle.tracer(False)
for x in range(500):
    turtle.forward(2*x)
    turtle.color(colors[x%len(colors)])
    turtle.left(91)
turtle.tracer(True)
turtle.done()