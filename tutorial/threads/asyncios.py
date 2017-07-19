import unittest
import asyncio
import threading
import time

""" asyncio的编程模型就是一个消息循环。
我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO"""


class PythonAsyncIO(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.loop = asyncio.get_event_loop()  # 获取EventLoop

	@classmethod
	def tearDownClass(cls):
		cls.loop.close()

	""" 把generator标记为coroutine类型
	async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
	把@asyncio.coroutine替换为async；
	把yield from替换为await; """

	async def hello(self):
		print("%s - %s: Hello world!" % (time.ctime(), threading.current_thread()))

		'''
		异步调用asyncio.sleep(3), yield from(await)语法可以让我们调用另一个generator
		耗时3秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
		'''
		r = await asyncio.sleep(3)
		print("%s - %s: Hello again" % (time.ctime(), threading.current_thread()))

	def test_eventloop(self):
		print('module asyncio: ')
		print(dir(asyncio))

		tasks = [self.hello(), self.hello()]  # 封装两个coroutine
		self.loop.run_until_complete(asyncio.wait(tasks))  # 执行协程coroutine

	async def wget(self, host):
		print('wget %s' % host)
		connect = asyncio.open_connection(host, 80)
		reader, writer = await connect  # 异步操作需要在coroutine中通过yield from(await)完成
		header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
		writer.write(header.encode('utf-8'))
		await writer.drain()
		while True:
			line = await reader.readline()
			if line == b'\r\n':
				break
			print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
			writer.close()

	def test_eventloop_with_connect(self):
		# 多个coroutine可以封装成一组Task然后并发执行
		tasks = [self.wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
		self.loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
	unittest.main()
