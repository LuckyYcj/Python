#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from urllib import request
import re


class Splider():
    # �����������ʵ�������   ����˳��  ʵ������--�������--������
    # page = 3
    # status = False
    __age = 2  # ˽�б����� �����ڲ����Է���

    # ���캯��
    def __init__(self):
        # ʵ�������� ÿ��ʵ�����е�
        self.page = 2
        self.status = True

    # ��������
    def __del__(self):
        print("end")

    def load_page(self):
        ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
        url = "http://222.186.10.159:468/article//index_"+str(self.page)+".html"
        request1 = request.Request(url, headers=ua_headers)
        res = request.urlopen(request1)
        html = res.read().decode("utf-8")
        print(html)
        # ������ʽƥ������
        p = re.compile('<div\sclass="desc">(.*?)</div>', re.S)
        contentlist = p.findall(html)
        print(contentlist)
        self.write_content(contentlist)

    def write_content(self, contentlist):  # ����__�ͱ��˽�з���
        print("����д��... ")
        with open('source/duanzi.txt', 'a') as f:
            f.write('\n\n'.join(contentlist))

    def startwork(self):
        while self.status:
            s.load_page()
            str1 = str(input("�Ƿ������ȡ����س����˳��밴Q��"))
            if str1 == "Q":
                self.status = False
            self.page = self.page + 1


s = Splider()
s.startwork()
