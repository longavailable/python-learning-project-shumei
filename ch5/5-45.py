# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 12:18:37 2025

@author: Xiaolong Liu
"""

import jieba

jieba.add_word('自胜者')   # 添加词库
jieba.del_word('知者')   # 删除词库

words = jieba.cut('知人者智，自知者明。胜人者有力，自胜者强。',cut_all=False)

print(type(words))

print(list(words))


words = jieba.cut('知人者智，自知者明。胜人者有力，自胜者强。',cut_all=True)

print(list(words))

words = jieba.cut('知人者智，自知者明。胜人者有力，自胜者强。',HMM=True)

print(list(words))


words = jieba.cut('知人者智，自知者明。胜人者有力，自胜者强。',HMM=False)

print(list(words))

# lcut 直接返回一个list
words = jieba.lcut('知人者智，自知者明。胜人者有力，自胜者强。',HMM=False)

print(words)