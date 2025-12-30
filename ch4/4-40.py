# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:34:52 2025

@author: 刘小龙
"""

import json

# 编码/序列化为JSON字符串
dict1 = {"name":"zhangping", "age":40}
print(dict1, type(dict1))

json_str1 = json.dumps(dict1)
print(json_str1, type(json_str1))

# 解码/反序列化 JSON字符串
json_str2 = '{"name":"zhangping", "age":35}'
dict2 = json.loads(json_str2)
print(dict2, type(dict2))

# 写入JSON文件
dict3 = {"name":"zhangping", "age":45}

with open('data.json', 'w') as f:   # w, r, a
    json.dump(dict3, f)

# 读取JSON文件
with open('data2.json', 'r') as f:
    dict4 = json.load(f)

print(dict4)
