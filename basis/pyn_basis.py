#!/usr/bin/env python
# -*- coding : utf-8 -*-
a = 1
if a == 1:
    print('a is 1')
else:
    print('a is not 1')
# 查看类型
print(type(a))

# 字符串
# 方法 find() index() capitalize()  首字母大写 upper() lower() swapcase() 大写转小写同时小写转大写 strip() 去除空格 lstrip() rstrip() 去除左右空格
# count() 统计字符出现次数 endwith() isdigit() 是否是数字 isalpha 是否是字母
str1 = 'abc'  # 重复输出 *4
print(str1)
str2 = "abc"
print(str2)
str3 = "a'bc'"
print(str3)
str4 = 'a"bc"'
print(str4)
print(str1[1])
print(str1[0:2])
# 修改字符串
list1 = list(str1)
print(list1)
list1[0] = 'A'
print(list1)
strMod = ''.join(list1)
print(strMod)

# 列表
# 方法 len() append() insert(index,"") 指定位置插入 index("") pop()删除末尾元素 pop(index) reverse() 反转
fruits = ['apple', 'pear', 'cherry', 'grape']
# 创建空列表
list1 = []
print(fruits[1])
print(fruits[len(fruits)-1])
# 遍历list
for var in fruits:
    print(var)

# 元祖
tu1 = ('a', 'b', 'c')
print(tu1[1:2])
# 删除元祖 del tu1， len()长度 max()最大值 min()最小值

# 字典
dict = {'id': 1, 'name': 'ycj'}   # 外面加上三引号就是json数据
print(dict['id'])
print(dict.keys())
print(dict.values())
print(dict)
moviesdict = {
    "芳华": "收到",
    "复活复": "的萨芬"
}
print(moviesdict.items())
print("芳华1" in moviesdict)

# 输入 输出
# 输入input()  输出print()
# age = input('Please input your age: ')
age = 45
print(age)
age = int(age)  # 强制转换类型
# help(print)  # 查看帮助
print('a', 'b', 'c', sep=',', end=';')

# while 循环
count = 0
while count < 10:
    print(count)
    count += 1

# 函数


def sum_func(a, b):
    '''
    加法
    :param a:
    :param b:
    :return:
    '''
    return a + b


print(sum_func(2, 4))


# 嵌套函数
def outer():
    def inner():
        print("inner")
    print("outer")


# 高阶函数
def outter(func):
    func()
    print("outter")


def intter():
    print("intter")


outter(intter)  # 不能添加小括号


# 装饰器  函数新加功能
def test1():
    print("this is test1")


def main(func):
    def deco():
        print("new function")
        func()
        print("new function2")
    return deco()


# test1 = main(test1)
# test1()

# @main  # test1 = main(test1)

user, pwd = 'admin', '123'


def login(func):
    def wrapper():
        username = input("请输入用户名：")
        password = input("请输入密码：")
        if username == user and password == pwd:
            print("login success")
            func()
        else:
            print("login failed")
    return wrapper


@login
def home():
    print("in the home")


home()

# 异常捕获
number1 = "hello"
try:
    number1=int(number1)
except Exception:
    print("出错咯")
else:
    print("代码没错的时候执行")
finally:
    print("不管错没错 都会执行")


# 面向对象编程


class Animal(object):
    def __init__(self, kind, voice):  # 构造函数
        self.kind = kind
        self.voice = voice

    def speak(self):
        print(self.voice)


cat = Animal('cat', '喵喵')
cat.speak()
