# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu
"""

import turtle as t

t.speed(10) # 0-10之间

t.color('red', 'yellow')    # 画笔颜色、填充颜色

t.begin_fill()

for i in range(40):
    
    t.forward(100)
    t.left(70)

t.end_fill()

t.done()    # turtle绘制最后一句，不结束会导致Tkinter程序卡死