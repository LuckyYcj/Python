#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from urllib import request, parse

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
# 用户输入
key = input("请输入翻译内容: ")
# 准备数据
formdata = {
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTON",
    "typoResult": "false"
}
data = parse.urlencode(formdata).encode("utf-8")
request1 = request.Request(url, headers=ua_headers, data=data)
print(request.urlopen(request1).read().decode("utf-8"))
