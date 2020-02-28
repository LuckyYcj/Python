#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-

# python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库
import xlrd
import xlwt
from xpinyin import Pinyin

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')
# 写入excel
# 参数对应 行, 列, 值
worksheet.write(1, 0, label='this is test')
# 保存
workbook.save('source/Excel_test.xls')

data = xlrd.open_workbook("source/textxlsx.xlsx")
table = data.sheets()[0]
print(table.row_values(0))
print(table.col_values(0))
print(table.nrows)
print(table.ncols)

for i in range(table.nrows):
    print(table.row_values(i))

print(table.cell(1, 2).value)

p = Pinyin()
print(p.get_pinyin("杨成杰").replace("-", " "))
