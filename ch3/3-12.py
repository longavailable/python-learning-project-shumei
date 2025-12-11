# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:41:45 2025

@author: 刘小龙
"""

# 关键字与软关键字

status = eval(input('请输入网页返回码:'))

# match-case 语句
match status:
    case 400:
        str1 = '400 Bad request'
    case 401:
        str1 = '401 Unauthorized'
    case 403:
        str1 = '403 Forbidden'
    case 404:
        str1 = '404 Not Found'
    case _:
        str1 = 'Unknown status coede'

print(status, str1)

# 多分支结构
if status == 400:
    str1 = '400 Bad request'
elif status == 401:
    str1 = '401 Unauthorized'
elif status == 403:
    str1 = '403 Forbidden'
elif status == 404:
    str1 = '404 Not Found'
else:
    str1 = 'Unknown status coede'

print(status, str1)