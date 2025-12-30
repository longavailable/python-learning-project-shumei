# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 14:56:51 2025

@author: 刘小龙
"""

import json

# 编码为JSON字符串
dict1 = {'name':'zp', 'age':'35'}
json_str = json.dumps(dict1)
print(json_str)

# 解码JSON字符串
json_str1 = '{"name":"zp","age":"40"}'
data = json.loads(json_str1)
print(data)

# 写入JSON文件
with open('data.json', 'w') as f:
    json.dump(dict1, f)


# 读取JSON文件
with open('data.json', 'r') as f:
    dict2 = json.load(f)
print(dict2)
