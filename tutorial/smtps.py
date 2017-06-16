# -*- coding: UTF-8 -*-

import smtplib, unittest
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

''' Python3 SMTP发送邮件 '''


class PythonSMTPLib(unittest.TestCase):
	smtp_info = {
		"hostname": "smtp.qq.com",
		"username": "82740301@qq.com",
		"password": "xpagwzokxmdzbjcb"  # 使用第三方SMTP服务发送, 获取授权码登录
	}
	mail_info = {
		"from": "82740301@qq.com",
		"to": "oliver19830714@gmail.com",
		"mail_encoding": "utf-8"
	}

	@classmethod
	def setUpClass(cls):
		# 这里使用SMTP_SSL就是默认使用465端口
		self.smtpobj = smtplib.SMTP_SSL(self.smtp_info["hostname"], timeout=5)
		self.smtpobj.set_debuglevel(1)
		self.smtpobj.ehlo(self.smtp_info["hostname"])
		self.smtpobj.login(self.smtp_info["username"], self.smtp_info["password"])

	@classmethod
	def tearDownClass(cls):
		self.smtpobj.quit()

	def send_email(self, format, subject, content):
		# 三个参数：第一个为文本内容，第二个设置文本格式，第三个 utf-8 设置编码
		msg = MIMEText(content, format, self.mail_info["mail_encoding"])
		msg["Subject"] = Header(subject, self.mail_info["mail_encoding"])
		msg["from"] = self.mail_info["from"]
		msg["to"] = self.mail_info["to"]

		try:
			self.smtpobj.sendmail(self.mail_info["from"], self.mail_info["to"], msg.as_string())
			print("邮件发送成功")
		except smtplib.SMTPException:
			print("Error: 无法发送邮件")

	def test_send_plain_mail(self):
		content = 'Plain Message using smtplib'
		subject = 'Python smtp testing with plain content'
		self.send_email('plain', subject, content)

	def test_send_html_mail(self):
		content = '''
		<p>HTML Message using smtplib</p>
		<p><a href="http://www.baidu.com">Test Link</a></p>
		'''
		subject = 'Python smtp testing with html content'
		self.send_email('html', subject, content)

	''' 发送带附件的邮件 '''

	def test_send_attachment_mail(self):
		# 创建一个带附件的实例
		msg = MIMEMultipart()
		msg['from'] = self.mail_info['from']
		msg['to'] = self.mail_info['to']
		subject = 'Python smtp testing with attached content'
		msg['subject'] = Header(subject, self.mail_info['mail_encoding'])

		# 邮件正文内容
		msg.attach(MIMEText('Attached Message using smtplib', 'plain', 'utf-8'))

		# 构造附件1
		attach1 = MIMEText(open('tmp/foo.txt', 'rb').read(), 'base', 'utf-8')
		attach1["Content-Type"] = 'application/octet-stream'
		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		attach1["Content-Disposition"] = 'attachment; filename="IAmFoo.txt"'
		msg.attach(attach1)

		# 构造附件2
		attach2 = MIMEText(open('tmp/apple.png', 'rb').read(), 'base', 'utf-8')
		attach2["Content-Type"] = 'application/octet-stream'
		attach2["Content-Disposition"] = 'attachment; filename="IAmApple.png"'
		msg.attach(attach2)

		self.smtpobj.sendmail(self.mail_info["from"], self.mail_info["to"], msg.as_string())

	''' 在 HTML 文本中添加图片 '''

	def test_send_image_mail(self):
		msg = MIMEMultipart('related')
		msg['from'] = self.mail_info['from']
		msg['to'] = self.mail_info['to']
		subject = 'Python smtp testing with image content'
		msg['subject'] = Header(subject, self.mail_info['mail_encoding'])

		msgAlternative = MIMEMultipart('alternative')
		msg.attach(msgAlternative)

		content = """
		<p>Image Message using smtplib</p>
		<p><a href="http://www.apple.com">Test Link</a></p>
		<p>图片演示：</p>
		<p><img src="cid:image1"></p>
		"""
		msgAlternative.attach(MIMEText(content, 'html', self.mail_info['mail_encoding']))

		# 指定图片为当前目录
		fp = open('tmp/apple.png', 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close()

		# 定义图片 ID，在 HTML 文本中引用
		msgImage.add_header('Content-ID', '<image1>')
		msg.attach(msgImage)

		self.smtpobj.sendmail(self.mail_info['from'], self.mail_info['to'], msg.as_string())


if __name__ == '__main__':
	unittest.main()
