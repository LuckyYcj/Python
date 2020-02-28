#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
'''
学生管理系统
展示系统功能给用户   print
添加学生，学生有姓名和学号  字典 {学号1：姓名，学号2：姓名，。。。}
删除学生，学生是存在的  if
修改学生，学生是存在的， if
查询学生，学生是存在的
显示所有学生，字典的遍历

只要用户不选择退出，就一直提示用户进行操作  while
'''
students={}

def showMenu():
    print('********** 学生管理系统 **********')
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询学生信息')
    print('5. 所有学生信息')
    print('6. 退出系统')
    print('*'*34)

def addStu():
    name=input('请输入学生的姓名：')
    stuID=input('请输入学生学号（学号必须唯一）：')
    while True:
        if stuID in students.keys():
            stuID=input('该学号已经存在，请重新输入：')
        else:
            break
    students[stuID]=name
    print('添加成功')

def deleteStu():
    stuID=input('请输入要删除的学生的学号：')
    while True:
        if stuID not in students.keys():
            stuID=input('该学号不存在，请重新输入：')
        else:
            break
    del(students[stuID])
    print('删除成功')


def updateStu():
    stuID=input('请输入要修改的学生的学号：')
    while True:
        if stuID not in students.keys():
            stuID=input('该学号不存在，请重新输入：')
        else:
            break
    name=input('请输入修改后的名字：')
    students[stuID]=name
    print('修改成功')

def queryStu():
    stuID=input('请输入要查询的学生的学号：')
    if stuID in students.keys():
        print('学号：'+stuID+'姓名：'+students[stuID])
    else:
        print('要查询的学生不存在。')

def showAll():
    print('当前系统中有以下学生：')
    for stuID in students.keys():
        print(stuID,':',students[stuID])


while True:
    showMenu()
    choice=int(input('请选择你要进行的操作：'))
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
        print('操作结束，退出系统')
        break
    else:
        print('你选择的功能不存在，请重新选择')
