import _thread
import threading
import time
import unittest

exitFlag = 0

''' Python3 多线程 '''


class PythonThreads(unittest.TestCase):

	@staticmethod
	def print_time(thread_name, delay):
		for i in range(5):
			time.sleep(delay)
			print("{}: {}".format(thread_name, time.ctime()))

	@unittest.skip
	def test_thread(self):
		try:
			# 创建两个线程
			_thread.start_new_thread(self.print_time, ('Thread-1', 2))
			_thread.start_new_thread(self.print_time, ('Thread-2', 3))
		except:
			print("Error: 无法启动线程")
		while True:
			pass

	def test_threading_lock(self):
		print('module _thread: ')
		print(dir(_thread))
		print('module threading: ')
		print(dir(threading))

		threads = []

		# 创建新线程
		threading1 = MyThread('101', 'Threading-1', 1)
		threading2 = MyThread('102', 'Threading-2', 2)

		# 开启新线程,即调用了线程的 run() 方法
		threading1.start()
		threading2.start()

		print('Current Thread: ' + repr(threading.current_thread()))  # 返回当前的线程变量
		print('Thread List: ' + repr(threading.enumerate()))  # 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程

		# 添加线程到线程列表
		threads.append(threading1)
		threads.append(threading2)

		'''join([time]): 等待至线程中止。这阻塞调用线程直至线程的join()
		方法被调用中止 - 正常退出或者抛出未处理的异常 - 或者是可选的超时发生'''
		for t in threads:
			t.join()

		print("退出主线程")


class MyThread(threading.Thread):
	threadLock = threading.Lock()

	def __init__(self, thread_id, name, interval):
		threading.Thread.__init__(self)
		self.threadID = thread_id
		self.name = name
		self.interval = interval

	def run(self):
		print('开始线程: ' + self.name)

		self.threadLock.acquire()  # 获取锁，用于线程同步
		self.print_time(self.name, self.interval, 5)
		self.threadLock.release()  # 释放锁，开启下一个线程

		print('退出线程: ' + self.name)

	@staticmethod
	def print_time(thread_name, delay, counter):
		while counter:
			global exitFlag
			if exitFlag:
				thread_name.exit()
			time.sleep(delay)
			print('{}: {}'.format(thread_name, time.ctime()))
			counter -= 1


if __name__ == '__main__':
	unittest.main()
