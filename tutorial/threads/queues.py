import queue
import threading
import time

"""
线程优先级队列（Queue）
Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue 模块中的常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""

exitFlag = 0


class MyThread(threading.Thread):
	def __init__(self, thread_id, name, q):
		threading.Thread.__init__(self)
		self.threadId = thread_id
		self.name = name
		self.q = q

	def run(self):
		print("开始线程: " + self.name)
		process_data(self.name, self.q)
		print("退出线程: " + self.name)


def process_data(thread_name, q):
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()  # 获取队列
			queueLock.release()
			print('{} processing: {}'.format(thread_name, data))
		else:
			queueLock.release()
		time.sleep(1)


print("module queue: ")
print(dir(queue))

thread_names = ['Threading-1', 'Threading-2', 'Threading-3']
texts = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
thread_id = 1

# 创建新线程
for name in thread_names:
	thread = MyThread(thread_id, name, workQueue)
	thread.start()
	threads.append(thread)
	thread_id += 1

# 填充队列
queueLock.acquire()
for text in texts:
	workQueue.put(text)  # 写入队列
queueLock.release()

# 等待队列清空
while not workQueue.empty():
	pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for thread in threads:
	thread.join()

print("退出主线程")
