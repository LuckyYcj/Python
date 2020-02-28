#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup
# pyquery

ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
url = "https://movie.douban.com/top250"
response = requests.get(url, headers=ua_headers)
html = response.text
# print(html)

soup = BeautifulSoup(html, "html.parser")  # lxml
# soup.find(condition)
# soup.find_all(condition)
# soup.select(css_selector)
movie_list = soup.find('ol', class_='grid_view')
movies = movie_list.find_all('li')
# print(movie_list)
# print(movies)

names = []
for movie in movies:
    movie_name = movie.find('span', class_='title').get_text()
    names.append(movie_name)

print(names)

with open('source/movies.txt', 'w') as f:
    for name in names:
        f.write(name+'\n')
