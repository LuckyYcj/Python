#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import random
my_num = random.randint(0, 100)
print('���������������ĸ����֣���-1�˳�')
# print(type(your_num))
# times=3
correct = False  #ע���Сд
while not correct:
    your_num = input()  # input�ķ���ֵ���ַ���
    if your_num == '-1':
        print('��ѡ�����˳���Ϸ�������˳���')
        break   #ѭ��������䣬�˳���ǰѭ��
    # times=times-1
    if your_num.isdigit():   #�ж��û�������Ƿ�������
        if int(your_num) == my_num:
            print('��ϲ�㣬����ˣ�')
            correct = True
        elif int(your_num)>my_num:
            print('���ˣ�̫����')
        else:
            print('���ˣ�̫С�ˣ�')
    else:
        print('����������')
