#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = '10086@139.com'
receivers = ['746804733@qq.com']

mas = MIMEText('宝贝','plain','utf-8')
mas['From'] = Header('中国移动','utf-8')
mas['To'] = Header('我试试呐','utf-8')
sub = '话费单'
mas['Subject'] = Header(sub,'utf-8')
try:
    smtpobj =smtplib.SMTP('localhost')
    smtpobj.sendmail(sender,receivers,mas.as_string())
    print('发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')