#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-


def set_func(fun):
    def call_func():
        print("Ȩ��1")
        print("Ȩ��2")
        fun()
    return call_func


@set_func
def test():
    print("���Ǻܰ����")


test()
test1 = set_func(test)  # ���ú���  ������������ ������   ���ǵ���
test1()

