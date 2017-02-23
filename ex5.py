# -*- coding:utf-8 -*-
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair ='Brown'


print "Let's talk about %r." % name # %s指代字符串变量,%r可以指代任何东西
print "He's %r inches tall." % height # %d指代数字变量
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# 问题：%r 用来做调试比较好，因为它会显示变量的原始数据，而%s 和其他符号则是用来向用户显示输出的。

# %%	百分号标记 #就是输出一个%
# %c	字符及其ASCII码
# %s	字符串
# %d	有符号整数(十进制)
# %u	无符号整数(十进制)
# %o	无符号整数(八进制)
# %x	无符号整数(十六进制)
# %X	无符号整数(十六进制大写字符)
# %e	浮点数字(科学计数法)
# %E	浮点数字(科学计数法，用E代替e)
# %f	浮点数字(用小数点符号)
# %g	浮点数字(根据值的大小采用%e或%f)
# %G	浮点数字(类似于%g)
# %p	指针(用十六进制打印值的内存地址)
# %n	存储输出字符的数量放进参数列表的下一个变量中
