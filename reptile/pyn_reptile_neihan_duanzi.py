#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from urllib import request
import re


class Splider():
    # 类变量：所有实例共享的   查找顺序  实例变量--》类变量--》父类
    # page = 3
    # status = False
    __age = 2  # 私有变量， 类中内部可以访问

    # 构造函数
    def __init__(self):
        # 实例变量： 每个实例独有的
        self.page = 2
        self.status = True

    # 析构函数
    def __del__(self):
        print("end")

    def load_page(self):
        ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
        url = "http://222.186.10.159:468/article//index_"+str(self.page)+".html"
        request1 = request.Request(url, headers=ua_headers)
        res = request.urlopen(request1)
        html = res.read().decode("utf-8")
        print(html)
        # 正则表达式匹配内容
        p = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
        contentlist = p.findall(html)
        print(contentlist)
        self.write_content(contentlist)

    def write_content(self, contentlist):  # 加上__就变成私有方法
        print("正在写入... ")
        with open('source/duanzi.txt', 'a') as f:
            f.write('\n\n'.join(contentlist))

    def startwork(self):
        while self.status:
            s.load_page()
            str1 = str(input("是否继续爬取，请回车（退出请按Q）"))
            if str1 == "Q":
                self.status = False
            self.page = self.page + 1


s = Splider()
s.startwork()
