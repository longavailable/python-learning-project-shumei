# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu
"""

import os

original_dir = os.getcwd()

print(original_dir)

os.chdir('d:\\')

new_dir = os.getcwd()

print(new_dir)

os.chdir(original_dir)

new_dir = os.getcwd()

print(new_dir)