#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
'''
ѧ������ϵͳ
չʾϵͳ���ܸ��û�   print
���ѧ����ѧ����������ѧ��  �ֵ� {ѧ��1��������ѧ��2��������������}
ɾ��ѧ����ѧ���Ǵ��ڵ�  if
�޸�ѧ����ѧ���Ǵ��ڵģ� if
��ѯѧ����ѧ���Ǵ��ڵ�
��ʾ����ѧ�����ֵ�ı���

ֻҪ�û���ѡ���˳�����һֱ��ʾ�û����в���  while
'''
students={}

def showMenu():
    print('********** ѧ������ϵͳ **********')
    print('1. ���ѧ����Ϣ')
    print('2. ɾ��ѧ����Ϣ')
    print('3. �޸�ѧ����Ϣ')
    print('4. ��ѯѧ����Ϣ')
    print('5. ����ѧ����Ϣ')
    print('6. �˳�ϵͳ')
    print('*'*34)

def addStu():
    name=input('������ѧ����������')
    stuID=input('������ѧ��ѧ�ţ�ѧ�ű���Ψһ����')
    while True:
        if stuID in students.keys():
            stuID=input('��ѧ���Ѿ����ڣ����������룺')
        else:
            break
    students[stuID]=name
    print('��ӳɹ�')

def deleteStu():
    stuID=input('������Ҫɾ����ѧ����ѧ�ţ�')
    while True:
        if stuID not in students.keys():
            stuID=input('��ѧ�Ų����ڣ����������룺')
        else:
            break
    del(students[stuID])
    print('ɾ���ɹ�')


def updateStu():
    stuID=input('������Ҫ�޸ĵ�ѧ����ѧ�ţ�')
    while True:
        if stuID not in students.keys():
            stuID=input('��ѧ�Ų����ڣ����������룺')
        else:
            break
    name=input('�������޸ĺ�����֣�')
    students[stuID]=name
    print('�޸ĳɹ�')

def queryStu():
    stuID=input('������Ҫ��ѯ��ѧ����ѧ�ţ�')
    if stuID in students.keys():
        print('ѧ�ţ�'+stuID+'������'+students[stuID])
    else:
        print('Ҫ��ѯ��ѧ�������ڡ�')

def showAll():
    print('��ǰϵͳ��������ѧ����')
    for stuID in students.keys():
        print(stuID,':',students[stuID])


while True:
    showMenu()
    choice=int(input('��ѡ����Ҫ���еĲ�����'))
    if choice==1:
        addStu()
    elif choice==2:
        deleteStu()
    elif choice==3:
        updateStu()
    elif choice==4:
        queryStu()
    elif choice==5:
        showAll()
    elif choice==6:
        print('�����������˳�ϵͳ')
        break
    else:
        print('��ѡ��Ĺ��ܲ����ڣ�������ѡ��')
