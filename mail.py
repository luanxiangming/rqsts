# -*- coding: UTF-8 -*-

import smtplib,sys
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

mail_info = {
    "from": "82740301@qq.com",
    "to": "18616762525@qq.com",
    "hostname": "smtp.qq.com",
    "username": "82740301@qq.com",
    # "password": "20011205",
    "password": "xpagwzokxmdzbjcb",
    # "password": "xwcpoqhnljiobjhc",
    "mail_encoding": "utf-8"
}

def send_mail(subject, content):
	#这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"], timeout=5)
    smtp.set_debuglevel(1)
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])
    msg = MIMEText(content, "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(subject, mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    smtp.quit()
