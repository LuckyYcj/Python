#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import requests
import jieba  # 结巴分词
from xpinyin import Pinyin
import re

p = Pinyin()
RhymeIndex = [( '1', [ 'a', 'ia', 'ua']), ( '2', [ 'ai', 'uai']), ( '3', [ 'an', 'ian', 'uan']),
( '4', [ 'ang', 'iang', 'uang']), ( '5', [ 'ao', 'iao']), ( '6', [ 'e', 'o', 'uo']), ( '7', [ 'ei', 'ui']),
( '8', [ 'en', 'in', 'un']), ( '9', [ 'eng', 'ing', 'ong', 'iong']), ( '10', [ 'er']), ( '11', [ 'i']),
( '12', [ 'ie', 'ye']), ( '13', [ 'ou', 'iu']), ( '14', [ 'u']), ( '16', [ 'ue']), ( '15', [ 'qu', 'xu', 'yu'])]

RhymeDct = { 'ui': '7', 'uan': '3', 'ian': '3', 'iu': '13', 'en': '8', 'ue': '16', 'ing': '9', 'a': '1', 'ei': '7',
'eng': '9', 'uo': '6', 'ye': '12', 'in': '8', 'ou': '13', 'ao': '5', 'uang': '4', 'ong': '9', 'ang': '4',
'ai': '2', 'ua': '1', 'uai': '2', 'an': '3', 'iao': '5', 'ia': '1', 'ie': '12', 'iong': '9', 'i': '11',
'er': '10', 'e': '6', 'u': '14', 'un': '8', 'iang': '4', 'o': '6', 'qu': '15', 'xu': '15', 'yu': '15'}


def wordcode(words):
    word_py = p.get_pinyin(words)
    wordslist = word_py.split('-')
    r = []
    for word in wordslist:
        while True:
            if not word:
                break
            token = RhymeDct.get(word, None)
            if token:
                r.append(token)
                break
            word = word[1:]
    if(len(r)) == len(words):
        return '-'.join(r)


def getkeyword():
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    ids = ["430053182", "33850315", "431795900"]
    with open("keyword.txt", "a") as f:
        f.write("[")
        for i in ids:
            lrcurl = "http://music.163.com/api/song/lyric?os=pc&id="+str(i)+"&lv=-1&kv=-1&tv=-1"
            req = requests.get(lrcurl, headers=ua_headers)
            dt = req.json()
            lrc = re.sub(u"\\[.*?]", "", dt['lrc']['lyric'])
            lrclist = list(jieba.cut(lrc,cut_all=True))
            for i in lrclist:
                if len(i) == 2:
                    if wordcode(i) != None:
                        f.write("{'"+wordcode(i)+"':'"+i+"'},")
        f.write("]")


# print(wordcode("杨成杰"))
# getkeyword()


def findkey(str):
    result = {}
    with open("keyword.txt") as f:
        list = eval(f.readlines()[0])
        for item in list:
            if item.get(str):
                key = item.get(str)
                number = result.get(key)
                if number != None and number >= 1:
                    result[key] = number + 1
                else:
                    result.update({key: 1})
    return result


key = input("please input key word:")
str1 = wordcode(key)
print(findkey(str1))
