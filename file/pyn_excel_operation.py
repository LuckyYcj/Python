#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-

# python����excel��Ҫ�õ�xlrd��xlwt�������⣬��xlrd�Ƕ�excel��xlwt��дexcel�Ŀ�
import xlrd
import xlwt
from xpinyin import Pinyin

# ����һ��workbook ���ñ���
workbook = xlwt.Workbook(encoding='utf-8')
# ����һ��worksheet
worksheet = workbook.add_sheet('My Worksheet')
# д��excel
# ������Ӧ ��, ��, ֵ
worksheet.write(1, 0, label='this is test')
# ����
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
print(p.get_pinyin("��ɽ�").replace("-", " "))
