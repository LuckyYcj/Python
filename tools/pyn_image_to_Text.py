#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from aip import AipOcr
import keyboard

print('---欢迎使用图片转文字的高级应用---')
# 定义常量
APP_ID = '17986057'
API_KEY = 'rWe9KCL4i7EmhD8dkXUaj4Mi'
SECRET_KEY = 'qOdvNg4PkcTDWUOHWhrr9Mny26I298eR'

# 初始化文字识别分类器
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


path = input('请输入要转为文字的图片路径：')
image = get_file_content(path)

# 调用通用文字识别, 图片参数为本地图片
client.basicGeneral(image)

# 如果有可选参数,定义参数变量
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
# 带参数调用通用文字识别, 图片参数为本地图片
result = client.basicGeneral(image, options)

# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://www.xxxxxx.com/img.jpg')
print('****以下为图片中的文字内容****\n')
for lis in result['words_result']:
    print(lis['words'])
input('\n识别完毕，操作完毕后按回车键退出-----')
