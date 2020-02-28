#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("mydata1.csv", header=None, encoding="gbk")


def get_city(val):
    city = val.split("|", 1)[0].split("-",1)[0]
    return city


df['city'] = df[3].map(get_city)


def get_money(val):
    try:
        money = re.findall('(\d+(\.\d+){0,1})', val)[0][0]
        money = float(money)
    except:
        return None
    if "千/月" in val:
        money /= 10
        return money
    if "万/月" in val:
        return money
    return None


df['money'] = df[1].map(get_money)
df.dropna(how="any", inplace=True)

df.boxplot('money')
plt.show()
df['money'].plot(kind="kde", ind=[0.8, 1, 1.2, 1.8, 2, 2.2, 2.5, 3, 3.5])
plt.show()

city_group = df.groupby('city')
plt.rcParams['font.sans-serif'] = ['SimHei']
city_group['money'].mean().sort_values(ascending=False).head(10).plot(kind="bar")
plt.show()
city_group['money'].count().sort_values(ascending=False).head(10).plot(kind="pie", subplots=True, autopct="%.2f%%", legend=False)
plt.show()

string = ''.join(list(df[2]))
string = re.sub("[\u4e00-\u9fa5]|\s", "", string)
wc = WordCloud(height=1000, width=1000)
mywords = wc.generate(string)
mywords.to_file("1.png")
