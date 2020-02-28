#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import pymysql


class MysqlHelper():
    def __init__(self, host, port, db, user, passwd, charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cur = self.conn.cursor()

    def closeconnect(self):
        self.cur.close()
        self.conn.close()

    def getalldata(self, sql):
        self.connect()
        result = self.cur.execute(sql)
        listdata = self.cur.fetchall()
        self.closeconnect()
        return listdata

