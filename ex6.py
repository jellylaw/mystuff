# -*- coding:utf-8 -*-
# 定义x为一个字符串
x = "There are %d types of people." % 10
# 将以下两个单词定义为字符串
binary = "binary" # 意思为二进制
do_not = "don't"
# 定义y为一个字符串，同时引用上述两个单词变量
y = "Those who know %s and those who %s." % (binary, do_not) # 把一个字符串放入另一个字符串1

# 打印输出x，y
print x
print y

# 打印字符串，字符串中有引用变量
print "I said: %r." % x # 把一个字符串放入另一个字符串2
print "I also said: '%s'." % y # 把一个字符串放入另一个字符串3

# 定义变量hilarious为false
hilarious = False
# 可以在定义变量时不在末尾加上格式化字符，而在打印中添加
joke_evaluation = "Isn't that joke so funny?! %r" # 把一个字符串放入另一个字符串4
# 打印时添加格式化字符
print joke_evaluation % hilarious

# 定义两个字符串变量
w = "This is the left side of..."
e = "a string with a right side."

# 两个字符串中间的“+”相当于连接符，且没有空格
print w + e
