#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from aip import AipOcr
import keyboard

print('---��ӭʹ��ͼƬת���ֵĸ߼�Ӧ��---')
# ���峣��
APP_ID = '17986057'
API_KEY = 'rWe9KCL4i7EmhD8dkXUaj4Mi'
SECRET_KEY = 'qOdvNg4PkcTDWUOHWhrr9Mny26I298eR'

# ��ʼ������ʶ�������
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# ��ȡͼƬ
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


path = input('������ҪתΪ���ֵ�ͼƬ·����')
image = get_file_content(path)

# ����ͨ������ʶ��, ͼƬ����Ϊ����ͼƬ
client.basicGeneral(image)

# ����п�ѡ����,�����������
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
# ����������ͨ������ʶ��, ͼƬ����Ϊ����ͼƬ
result = client.basicGeneral(image, options)

# ���ͼƬ��url ����ʾ������
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')
print('****����ΪͼƬ�е���������****\n')
for lis in result['words_result']:
    print(lis['words'])
input('\nʶ����ϣ�������Ϻ󰴻س����˳�-----')
