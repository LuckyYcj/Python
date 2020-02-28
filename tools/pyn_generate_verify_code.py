#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
'''
1. 画一张空白的画
2. 画底色，给每一个像素填充一个颜色，颜色随机  ——函数
3. 往画上写字，字是随机的（函数），字的颜色也是随机的（函数）
4. 保存图片

pillow
pip install pillow   #这是命令，这是命令，这是命令，在命令行执行。
'''
from PIL import Image,ImageDraw,ImageFont
import numpy as np

def random_char():
    '''
    生成随机字符
    unicode
    大写字母  65-90,小写字母: 97-122，数字：48-57，汉字：19968-40895
    chr(65)=A
    :return:
    '''
    mylist=[]
    mylist.extend([i for i in range(48,58)])
    mylist.extend([i for i in range(65,91)])
    mylist.extend([i for i in range(97,123)])
   # mylist.extend([i for i in range(19968,20000)]) #汉字，占的比例太大，容易导致取值偏向汉字
    print(mylist[1:9])
    index = np.random.randint(0,len(mylist)-1)
    print(index)
    mychar = chr(mylist[index])
    print(mychar)
    return mychar

def char_color():

    return (np.random.randint(10, 120), np.random.randint(10, 120), np.random.randint(10, 120))

def bg_color():
    return (np.random.randint(122,255),np.random.randint(122,255),np.random.randint(122,255))

def gen_code():
    #画一张空白图片
    w,h=200,50
    image=Image.new('RGB',(w,h),(255,255,255))
    #填充像素
    draw=ImageDraw.Draw(image)
    for width in range(w):
        for height in range(h):
            draw.point((width,height),bg_color())
    #随机写四个字符  BROADW.TTF
    myfont=ImageFont.truetype('simsun.ttc',36)  #设置字体
    for i in range(4):
        draw.text((50*i+10,10),random_char(),fill=char_color(),font=myfont)
    #保存图片
    image.save('code_new.jpg')

if __name__=='__main__':
    gen_code()

