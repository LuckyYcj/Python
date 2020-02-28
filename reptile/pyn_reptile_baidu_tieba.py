#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
# 指定爬虫爬取文件， 文件下载
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
    print("下载完毕")


def tieba_spider(url, beginpage, endpage):
    for page in range(beginpage, endpage + 1):
        pn = (page - 1) * 50
        filename = "source/第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        html = load_page(fullurl, filename)
        write_page(html, filename)


# 入口
kw = input("请输入爬去的贴吧名字: ")
begin_page = int(input("请输入起始页: "))
end_page = int(input("请输入结束页: "))

url = "http://tieba.baidu.com/f"
key = parse.urlencode({"kw": kw})
full_url = url + key
tieba_spider(full_url, begin_page, end_page)
