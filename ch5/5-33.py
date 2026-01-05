# -*- coding: utf-8 -*-
"""
Created on Mon Jan  5 15:32:22 2026

@author: 刘小龙
"""

def outer():
    def inner():
        print('inner:内以养志')
    print('outer:外以知人')
    inner()    
outer()

# %%

def say_hello():
    print('Hello!')

def my_decorator(func):
    def wrapper():
        print('开始执行')
        func()
        print('执行结束')
    return wrapper

#
say_hello2 = my_decorator(say_hello)    # 赋值符号起重命名作用
say_hello2()

say_hello3 = my_decorator(outer)
say_hello3()
# %%

def my_decorator888(func):
    def wrapper():
        print('开始执行1')
        func()
        print('执行结束1')
    return wrapper

@my_decorator888
def say_hello():
    print('Hello2')
    
say_hello()
    
