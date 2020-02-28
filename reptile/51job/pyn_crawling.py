#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from urllib import request
import lxml.html as html
import csv

links = []


def get_list_page(page):
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,"+str(page)+".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    req = request.Request(url, headers=ua_headers)
    res = request.urlopen(req)
    data = res.read().decode('GBK', errors='ignore')
    doc = html.document_fromstring(data)
    xpath = "//div[@class='el'] /p/span/a/@href"
    links.append(doc.xpath(xpath))


def get_page_details():
    lf = open("mydata1.csv", "w")
    csv_writer = csv.writer(lf)
    for link in links:
        print(link)
        # 提取详细页信息
        for each_link in link:
            try:
                f = request.urlopen(each_link)
                detaildata = f.read().decode('GBK', errors='ignore')
                detail_doc = html.document_fromstring(detaildata)
            except Exception:
                print("error")
                continue

            jobname_xpath = "//h1/@title"
            jobmoney_xpath = "//div[@class='cn']/strong/text()"
            jobrequire_xpath = "//div[@class='bmsg job_msg inbox']"
            jobother_xpath = "//p[@class='msg ltype']/@title"

            try:
                jobname = detail_doc.xpath(jobname_xpath)[0]
                jobmoney = detail_doc.xpath(jobmoney_xpath)[0]
                jobrequire = detail_doc.xpath(jobrequire_xpath)[0].text_content().replace("\xa0", "")
                jobother = detail_doc.xpath(jobother_xpath)[0].replace("\xa0", "")
                csv_writer.writerow([jobname, jobmoney, jobrequire, jobother])
            except Exception:
                print("error")
    lf.close()


def main_method():
    #  获取所有列表信息
    i = 1
    while i <= 10:
        get_list_page(i)
        i = i+1

    get_page_details()


main_method()
