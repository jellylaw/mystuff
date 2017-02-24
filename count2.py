# -*- coding: utf-8 -*-

from  collections  import Counter
import sys,re
import codecs
# 读取文本内容，编码为汉字
txt = codecs.open("happiness_seg.txt","r",'utf-8')
# 将文本内容拆分，并存放在list中
List = txt.read().split(" ")

# Counter函数
c = Counter()
# 将list列表中的每一个量都执行以下操作:
#若相邻两词的长度都等于2，则将这相邻两词相加并存储，词频统计+1
for i in range(0,(len(List) - 1)) :
    if len(List[i]) == 2 and len(List[i + 1]) == 2:
        double_words = List[i] + List[i + 1]
        c[double_words] = c[double_words] + 1

# 频率最高的前10个词组
most_words = c.most_common(10)
# 分别输出
for i in range(len(most_words)):
    print most_words[i][0],most_words[i][1]
