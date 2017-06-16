"""
Python对协程的支持是通过generator实现的。
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
"""


# consumer函数是一个generator
def consumer():
	r = ''
	while True:
		n = yield r  # 3.通过yield拿到消息，处理，又通过yield把结果传回
		if not n:
			return
		print('[CONSUMER] Consuming %s..' % n)
		r = '200 OK'


def produce(c):
	c.send(None)  # 1.启动生成器
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)  # 2.切换到consumer执行
		print('[PRODUCER] Consumer return: %s' % r)  # 4.拿到consumer处理的结果，继续生产下一条消息
	c.close()  # 5.通过c.close()关闭consumer，整个过程结束


c = consumer()
produce(c)
