#!/usr/bin/env python
# -*- coding : utf-8 -*-
# 文件读写 open()  readlines() readline() write() close()
f1 = open(r'D:\python\document\python_code\testFile.txt')  # 'r'只读 '  w'清空再写   'a'追加    'x' 新建   '+'读写
lines = f1.readlines()
print(lines)
f1.close()

f2 = open(r'D:\python\document\python_code\testFile.txt', 'w')
f2.write('67890')
f2.close()

f3 = open(r'D:\python\document\python_code\testFile.txt', 'w')
linesText = ['a\n', 'b\n', '100\n']
f3.writelines(linesText)
f3.close()
