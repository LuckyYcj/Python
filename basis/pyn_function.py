#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-


def set_func(fun):
    def call_func():
        print("权限1")
        print("权限2")
        fun()
    return call_func


@set_func
def test():
    print("你们很棒的唷")


test()
test1 = set_func(test)  # 调用函数  方法不带括号 是引用   不是调用
test1()

