#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
# ָ��������ȡ�ļ��� �ļ�����
from urllib import request, parse


def load_page(fullurl, filename):
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    req = request.Request(fullurl, headers=ua_headers)
    html = request.urlopen(req).read()
    return html


def write_page(html, filename):
    print(html)
    print(filename)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(html.decode('utf8', 'ignore'))
    print("�������")


def tieba_spider(url, beginpage, endpage):
    for page in range(beginpage, endpage + 1):
        pn = (page - 1) * 50
        filename = "source/��" + str(page) + "ҳ.html"
        fullurl = url + "&pn=" + str(pn)
        html = load_page(fullurl, filename)
        write_page(html, filename)


# ���
kw = input("��������ȥ����������: ")
begin_page = int(input("��������ʼҳ: "))
end_page = int(input("���������ҳ: "))

url = "http://tieba.baidu.com/f"
key = parse.urlencode({"kw": kw})
full_url = url + key
tieba_spider(full_url, begin_page, end_page)
