from wechat_sender import *
import time
import logging
from tutorial.wechat import config

logger = logging.getLogger(__name__)


def init_logger():
	"""
	wechat_sender 的 LoggingHandler 对象，可以使用 logging.addHandler() 的方式快速使外部应用支持微信日志输出
	receiver – (选填|str) - 接收者，wxpy 的 puid 或 微信名、昵称等，不填将发送至 default_receiver
	"""
	sender_logger = LoggingSenderHandler('sender', receiver='家庭聊天', level=logging.WARNING)
	logger.addHandler(sender_logger)


def send_p2p():
	"""
	所有未指定接收者的 Sender 都将把消息发给默认接收者, 不填为当前 bot 对象的文件接收者
	"""
	Sender().send('[{}]Hello from wx_sender...'.format(time.ctime()))
	logger.warning("send_p2p success")


def send_group():
	"""向 group 发送消息 """
	Sender(receivers=config.group).send('[{}]Hello from wx_sender...'.format(time.ctime()))
	logger.warning("send_group success")

init_logger()
# send_p2p()
send_group()
