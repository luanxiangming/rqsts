from wechat_sender import listen
from wxpy import *
from tutorial.wechat import config


def sender_outside():
	# 登录微信并启动 wechat_sender 服务, cache_path为 `True` 时，使用默认的缓存路径 'wxpy.pkl'
	bot = Bot(cache_path=True, console_qr=True)
	bot.enable_puid()
	me = bot.friends().search(config.me)[0]
	to = bot.friends().search(config.to)[0]
	group = bot.groups().search(config.group)[0]

	print('发送者: ' + me.name + '(' + me.puid + ')')
	print('接收者: ' + to.name + '(' + to.puid + ')')
	print('接收组: ' + group.name + '(' + group.puid + ')')

	'''
	之后 wechat_sender 将持续运行等待接收外部消息
	当 listen() 传入 receivers 时会把第一个 receiver 当做默认接收者，所有未指定接收者的 Sender 都将把消息发给默认接收者
	如果不传receivers，消息将通过登录微信的文件助手发送给你
	wechat_sender 的状态报告，定时向 status_receiver 发送状态信息
	不指定 status_receiver 时状态报告将发送到默认接收者, 默认每隔一小时进行一次状态报告
	
	注意：receivers和status_receiver不能是发送者自己
	'''
	listen(bot, receivers=[to, group], status_report=True, status_receiver=me)  # to是默认接收者


sender_outside()
