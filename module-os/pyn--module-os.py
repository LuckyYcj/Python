#!/usr/bin/env python
# -*- coding : utf-8 -*-
#  第一种 调用方法不一样
# import module1
# module1.say()

# 第二种
# from module1 import say as newsay
# from module1 import *
# say()

# 内置模块
# datetime
import datetime
import random
import sys
import os
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now()+datetime.timedelta(days=10))
print(datetime.datetime.now()+datetime.timedelta(hours=10))

from datetime import datetime
print(datetime.now())

# random
print(random.random())
print(random.randint(0, 100))
print(random.randrange(0, 100))
print(random.choice('ycj'))
print(random.choice(["aa", "bb", "cc"]))
print(random.randrange(1, 9000)+1000)  # 生成四位随机验证码

# sys
print(sys.platform)
print(sys.path)
print(sys.builtin_module_names)

# module-os
print(os.name)
print(os.getcwd())
# module-os.rename("", "")
print(os.listdir())
print(os.system("dir"))  # 调用系统命令
