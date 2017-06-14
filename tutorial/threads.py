import unittest, _thread, time, threading, queue

exitFlag = 0

''' Python3 多线程 '''
class PythonThreads(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def print_time(self, threadName, delay):
		for i in range(5):
			time.sleep(delay)
			print("{}: {}".format(threadName, time.ctime()))

	def test_thread(self):
		print('module _thread: ')
		print(dir(_thread))
		try:
			_thread.start_new_thread(self.print_time, ('Thread-1', 2))
			_thread.start_new_thread(self.print_time, ('Thread-2', 3))
		except:
			print("Error: 无法启动线程")
		while True:
			pass


	def test_threading_lock(self):
		threads = []

		# 创建新线程
		threading1 = myThread('101', 'Threading-1', 1)
		threading2 = myThread('102', 'Threading-2', 2)

		# 开启新线程
		threading1.start()
		threading2.start()

		# 添加线程到线程列表
		threads.append(threading1)
		threads.append(threading2)

		'''join([time]): 等待至线程中止。这阻塞调用线程直至线程的join()
		方法被调用中止 - 正常退出或者抛出未处理的异常 - 或者是可选的超时发生'''
		for t in threads:
			t.join()

		print("退出主线程")


class myThread(threading.Thread):
	threadLock = threading.Lock()

	def __init__(self, threadID, name, interval):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.interval = interval

	def run(self):
		print('开始线程: ' + self.name)
		self.print_time(self.name, self.interval, 5)
		print('退出线程: ' + self.name)

	def print_time(self, threadname, delay, counter):
		self.threadLock.acquire()  # 获取锁，用于线程同步
		while counter:
			global exitFlag
			if exitFlag:
				threadname.exit()
			time.sleep(delay)
			print('{}: {}'.format(threadname, time.ctime()))
			counter -= 1
		self.threadLock.release() # 释放锁，开启下一个线程


if __name__ == '__main__':
	unittest.main()