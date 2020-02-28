#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import random
my_num = random.randint(0, 100)
print('你猜我心里想的是哪个数字？按-1退出')
# print(type(your_num))
# times=3
correct = False  #注意大小写
while not correct:
    your_num = input()  # input的返回值是字符串
    if your_num == '-1':
        print('你选择了退出游戏，现在退出。')
        break   #循环控制语句，退出当前循环
    # times=times-1
    if your_num.isdigit():   #判断用户输入的是否是数字
        if int(your_num) == my_num:
            print('恭喜你，答对了！')
            correct = True
        elif int(your_num)>my_num:
            print('错了，太大了')
        else:
            print('错了，太小了！')
    else:
        print('请输入数字')
