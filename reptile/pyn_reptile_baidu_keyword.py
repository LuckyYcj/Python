#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from urllib import request, parse

ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
url = "https://www.baidu.com/s"
keyword = input("请输入关键字： ")
wd = {"wd": keyword}
wd = parse.urlencode(wd)
full_url = url + "?" + wd
print(full_url)
req = request.Request(full_url, headers=ua_headers)
response = request.urlopen(req)
html = response.read()
print(html.decode(encoding="utf-8"))
