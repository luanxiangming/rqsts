import os
import logging
import multiprocessing


def init():
	print('\nmodule multiprocessing:')
	print(dir(multiprocessing))
	print('\nclass multiprocessing.Process:')
	print(dir(multiprocessing.Process))
	print('\nclass multiprocessing.Queue:')
	print(dir(multiprocessing.Queue))

	multiprocessing.log_to_stderr()
	logger = multiprocessing.get_logger()
	logger.setLevel(logging.INFO)


def doubler(number):
	""" A doubling function that can be used by a process """
	result = number * 2
	# process = os.getpid()
	process = multiprocessing.current_process().name  # current_process获取正在调用我们的函数的线程的名字
	print('{0} get doubled to {1} by process: {2}'.format(number, result, process))


def printer(item, lock):
	lock.acquire()
	try:
		print(item)
	finally:
		lock.release()


def try_process():
	numbers = [5, 10, 15, 20, 25]
	processes = []
	for index, number in enumerate(numbers):
		# Process这个类和threading模块中的Thread类很像
		process = multiprocessing.Process(target=doubler, args=(number,))
		processes.append(process)
		process.start()

	# 自定义进程名字，默认情况下，multiprocessing模块给每个进程分配了一个编号，而该编号被用来组成进程的名字的一部分
	process = multiprocessing.Process(target=doubler, name='Test', args=(100,))
	processes.append(process)
	process.start()

	for process in processes:
		process.join()  # 调用每个进程的join()方法，该方法告诉Python等待进程直到它结束。如果你需要结束一个进程，你可以调用它的terminate()方法


def try_lock():
	lock = multiprocessing.Lock()
	items = ['tango', 'foxtrot', 10]

	# 这里并没有调用join()方法。取而代之的：当它退出，父线程将自动调用join()方法
	for item in items:
		p = multiprocessing.Process(target=printer, args=(item, lock))
		p.start()


def try_pool():
	""" Pool类被用来代表一个工作进程池。它有让你将任务转移到工作进程的方法 """
	numbers = [100, 200, 300]
	pool = multiprocessing.Pool(processes=3)  # 一个Pool的实例被创建，并且该实例创建了3个工作进程
	print(pool.map(doubler, numbers))  # map方法将一个函数和一个可迭代对象映射到每个进程

	# 也能通过apply_async方法获得池中进程的运行结果
	result = pool.apply_async(doubler, (50,))
	print(result.get(timeout=1))


def producer(data, q):
	""" Creates data to be consumed and waits for the consumer to finish processing """
	print('Creating data and putting it on the queue')
	for item in data:
		q.put(item)


def consumer(q):
	""" Consumes some data and works on it. In this case, all it does is double the input """
	sentinel = object()
	while True:
		data = q.get()
		print('data found to be processed: {}'.format(data))
		processed = data * 2
		print(processed)
		if data is sentinel:
			break


def try_queue():
	q = multiprocessing.Queue()
	data = [1, 5, 10, 20]

	process_1 = multiprocessing.Process(target=producer, name="PRODUCER", args=(data, q))
	process_2 = multiprocessing.Process(target=consumer, name="CONSUMER", args=(q,))

	process_1.start()
	process_2.start()

	q.close()
	q.join_thread()

	# 在进程对象上调用join()方法，而不是在Queue本身上调用
	process_1.join()
	process_2.join()


if __name__ == '__main__':
	init()
	try_process()
	try_lock()
	try_pool()
	try_queue()
