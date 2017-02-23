# -*- coding:utf-8 -*-
# "="的意思是为变量命名，以下每一行都是新定义的一个变量，而“==”是检查两边数值是否相等。
# 车辆=100
cars = 100
# 每辆车的载客数=4，此处使用浮点数和非浮点数计算结果没有误差，因为商是整数
space_in_a_car = 4.0
# 司机=30
drivers = 30
# 乘客=90
passengers = 90
# 空闲的车=总车辆-司机数
cars_not_driven = cars - drivers
# 正常运营的车=司机数
cars_driven = drivers
# 可以载客的人数=正常运营的车*每辆车的载客数
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车携带的乘客=总乘客/正常运营的车
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
