# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 2025

@author: 刘小龙

Content: 利用随机数来互动
"""

import random
import csv

# 输入文件的路径
file = 'data/004-random-znjz2321.csv'

# 读取文件
with open(file, 'r', encoding='utf-8') as f:
    namelist = list(csv.reader(f, delimiter=','))

namelist = namelist[1:]
'''
print(namelist)
print(len(namelist))
print(namelist[0])
'''
fout = 'data/004-20241120-出勤.csv'

#breakpoint()

with open(fout, 'w', encoding='utf-8', newline='') as f:

    # 定义一支笔
    writer = csv.writer(f, delimiter=',')

    # 写入表头
    writer.writerow([ '学号', '姓名', '出勤', '得分'])

    while True:
        index = random.randrange(0,len(namelist))   # 前闭后开区间

        # 输出随机同学及其学号到屏幕
        print('学号：', namelist[index][0], '姓名：', namelist[index][1])

        # 提示教师如何录入出勤情况
        print('请输入该生出勤情况：出勤(C)/公假(G)/事假(S)/缺勤(Q)')  # 1/0.9/0.8/0

        # 获取用户在桌面的输入
        status = str(input())[0]

        #print(status, type(status))
        if status.upper() == 'C': attend_status, att_score = '出勤', 1
        '''
        if status.upper() == 'C':
            attend_status = '出勤'
            attend_score = 1
        '''

        if status.upper() == 'G': attend_status, att_score = '公假', 0.9
        if status.upper() == 'S': attend_status, att_score = '事假', 0.8
        if status.upper() == 'Q': attend_status, att_score = '缺勤', 0
        #print(attend_status, att_score)

        # 写入出勤情况
        writer.writerow( namelist[index]  + [attend_status, att_score])

        # 移除已经点过名的同学
        namelist.remove(namelist[index])

        # 名单结束，跳出循环
        if len(namelist) < 1: exit()