#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
'''
1. ��һ�ſհ׵Ļ�
2. ����ɫ����ÿһ���������һ����ɫ����ɫ���  ��������
3. ������д�֣���������ģ����������ֵ���ɫҲ������ģ�������
4. ����ͼƬ

pillow
pip install pillow   #�����������������������������ִ�С�
'''
from PIL import Image,ImageDraw,ImageFont
import numpy as np

def random_char():
    '''
    ��������ַ�
    unicode
    ��д��ĸ  65-90,Сд��ĸ: 97-122�����֣�48-57�����֣�19968-40895
    chr(65)=A
    :return:
    '''
    mylist=[]
    mylist.extend([i for i in range(48,58)])
    mylist.extend([i for i in range(65,91)])
    mylist.extend([i for i in range(97,123)])
   # mylist.extend([i for i in range(19968,20000)]) #���֣�ռ�ı���̫�����׵���ȡֵƫ����
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
    #��һ�ſհ�ͼƬ
    w,h=200,50
    image=Image.new('RGB',(w,h),(255,255,255))
    #�������
    draw=ImageDraw.Draw(image)
    for width in range(w):
        for height in range(h):
            draw.point((width,height),bg_color())
    #���д�ĸ��ַ�  BROADW.TTF
    myfont=ImageFont.truetype('simsun.ttc',36)  #��������
    for i in range(4):
        draw.text((50*i+10,10),random_char(),fill=char_color(),font=myfont)
    #����ͼƬ
    image.save('code_new.jpg')

if __name__=='__main__':
    gen_code()

