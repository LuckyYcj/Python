#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
from pyn_database_helper import *
# 创建连接
conn = pymysql.connect(host="localhost", port=3306, db="test", user="root", passwd="Pa55w0rd", charset="utf8")
# cur 对数据库的封装
cur = conn.cursor()

# select
result = cur.execute("select * from spring_mvc_user")
resultlist = cur.fetchall()
# print(result)
# print(resultlist)

# add
# cur.execute("insert into spring_mvc_user values (4,'tett','ttt','tttt')")
# conn.commit()

# update
# cur.execute("insert into spring_mvc_user values (4,'tett','ttt','tttt')")
# conn.commit()

# delete
# cur.execute("insert into spring_mvc_user values (4,'tett','ttt','tttt')")
# conn.commit()

dbhelper = MysqlHelper(host="localhost", port=3306, db="test", user="root", passwd="Pa55w0rd", charset="utf8")
print(dbhelper.getalldata("select * from spring_mvc_user"))
