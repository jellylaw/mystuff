# -*- coding:utf-8 -*-
# 从系统中导入参数变量模块
from sys import argv

# script的意思是文件名，即ex15.py；运行这个文件时需要输入一个参数值
script, filename = argv

# 打开文件
txt = open(filename)

# 打印这里是你的文件，并加上运行时输入的文件名
print "Here's your file %r:" % filename
# .read函数可以直接读取文件
print txt.read()

# 再次打印文件
print "Type the filename again:"
# 采用raw_input函数读取用户输入的文件名
file_again = raw_input("> ")

# 打开用户输入的文件名
txt_again = open(file_again)

# 再次打印
print txt_again.read()

# 关闭文件。是否两个都要关闭？
print txt.close()
print txt_again.close()
