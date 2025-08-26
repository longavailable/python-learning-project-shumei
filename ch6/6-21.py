# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu
"""

import csv

# 创建一个 CSV 文件
with open('6-21.csv', 'w', newline='') as csvfile:
    # 指定 quotechar 为单引号
    writer = csv.writer(csvfile, quotechar="'")
    
    # 写入一些数据
    writer.writerow(['Name', 'Age', 'Description'])
    writer.writerow(['Alice', 25, 'Alice is a developer.'])
    writer.writerow(['Bob', 30, "Bob's favorite hobby is reading."])
    writer.writerow(['Charlie', 35, 'Charlie, who is a teacher, loves to travel.'])

# 读取并打印 CSV 文件内容
with open('6-21.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, quotechar="'")
    for row in reader:
        print(row)