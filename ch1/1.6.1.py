# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 15:27:05 2025

@author: 刘小龙
"""

import time

str1 = """
    中国共产党已走过百年奋斗历程。我们党立志于中华民族千秋伟业，致力于人类和平与
发展崇高事业，责任无比重大，使命无上光荣。全党同志务必不忘初心、牢记使命，务必谦
虚谨慎、艰苦奋斗，务必敢于斗争、善于斗争，坚定历史自信，增强历史主动，谱写新时代
中国特色社会主义更加绚丽的华章。
"""

for i in str1:
    #print(i, end="")
    print(i, end="", flush=True)
    time.sleep(0.1)
print()