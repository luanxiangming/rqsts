"""
Python对协程的支持是通过generator实现的。
在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
"""


# consumer函数是一个generator
def consumer():
	r = 'a'  # 2.只有第一次会执行(启动生成器), 之后再调用生成器就会从yield处执行
	print('*****生成器启动*****')
	while True:
		''' yield不但可以返回一个值，它还可以接收调用者发出的参数 '''
		n = yield r  # 4.再次执行时从这里的yield继续执行, 将把produce传入的参数n赋给局部变量n, 下轮循环再次遇到yield就会就将r返回给produce函数
		if not n:
			return
		print('[CONSUMER] Consuming %s..' % n)  # 5.由于生成器在启动的时候遇到上面的yield就返回了, 所以第一次不会执行这条语句, 之后每次都会被执行
		r = '200 OK'  # 6.因为yield r 所以这个r会在下一次循环被返回给produce函数


def produce(c):
	c.send(None)  # 1.启动生成器, 等于next(c)
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)  # 3.切换到consumer执行, 获取生成器consumer中由yield语句返回的下一个值
		print('[PRODUCER] Consumer return: %s' % r)  # 7.拿到consumer处理的结果，继续生产下一条消息
	c.close()  # 8.通过c.close()关闭consumer，整个过程结束


c = consumer()  # 并不会启动生成器, 只是将c变为一个生成器
produce(c)  # 协程处GEN_CREATE（等待开始状态）
