#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'jcymini@163.com'
my_pass = 'LuckYcj1124'
to_user = '791461309@qq.com'


def senderemial():
    ret = True
    try:
        msg = MIMEText("你是我的小苹果，怎么爱你都不嫌多", "plain", "utf-8")
        msg['From'] = formataddr(["你的老公大人", my_sender])
        msg['To'] = formataddr(["小老婆", to_user])
        msg['Subject'] = "小小小老婆"

        smtp_server = 'smtp.163.com'
        smtp_port = 465
        '''
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        '''
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [to_user], msg.as_string())
        server.quit()
    except Exception as ex:
        print(ex)
        ret = False
    return ret


i = 0
while i < 10:
    ret = senderemial()
    if ret:
        print("发送成功")
    else:
        print("发送失败")
    i = i + 1
