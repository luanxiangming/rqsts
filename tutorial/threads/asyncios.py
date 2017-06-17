import unittest
import asyncio
import threading

""" asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO"""


class PythonAsyncIO(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.loop = asyncio.get_event_loop()  # 获取EventLoop

	@classmethod
	def tearDownClass(cls):
		cls.loop.close()

	# 把generator标记为coroutine类型
	@asyncio.coroutine
	def hello(self):
		print("%s: Hello world!" % threading.current_thread())

		'''
		异步调用asyncio.sleep(1), yield from语法可以让我们方便地调用另一个generator
		耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
		'''
		r = yield from asyncio.sleep(1)
		print("%s: Hello again" % threading.current_thread())

	def test_eventloop(self):
		print('module asyncio: ')
		print(dir(asyncio))

		tasks = [self.hello(), self.hello()]  # 封装两个coroutine
		self.loop.run_until_complete(asyncio.wait(tasks))  # 执行协程coroutine

	@asyncio.coroutine
	def wget(self, host):
		print('wget %s' % host)
		connect = asyncio.open_connection(host, 80)
		reader, writer = yield from connect  # 异步操作需要在coroutine中通过yield from完成
		header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
		writer.write(header.encode('utf-8'))
		yield from writer.drain()
		while True:
			line = yield from reader.readline()
			if line == b'\r\n':
				break
			print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
			writer.close()

	def test_eventloop_with_connect(self):
		# 多个coroutine可以封装成一组Task然后并发执行。
		tasks = [self.wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
		self.loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
	unittest.main()
