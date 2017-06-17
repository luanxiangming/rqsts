import unittest
import sys
import itertools


class PythonIterators(unittest.TestCase):
	"""
	迭代器是一个可以记住遍历的位置的对象。
	迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
	"""

	def setUp(self):
		self.list = [1, 2, 3, 4]

	def tearDown(self):
		pass

	def test_iter_next(self):
		it = iter(self.list)  # 创建迭代器对象
		self.assertEqual(next(it), 1)
		self.assertEqual(next(it), 2)

	def test_loop_for(self):
		it = iter(self.list)
		for i in it:
			print(i, end=',')

	def test_loop_while(self):
		it = iter(self.list)
		while True:
			try:
				print(next(it))
			except StopIteration:
				print(sys.exc_info())
				return


class PythonGenerators(unittest.TestCase):
	"""
	在 Python 中，使用了 yield 的函数被称为生成器（generator）。
	跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
	在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行next()方法时从当前位置继续运行。
	"""

	@staticmethod
	def fibonacci(n):  # 生成器函数 - 斐波那契
		a, b, counter = 0, 1, 0
		while True:
			if counter > n:
				return
			yield a
			a, b = b, a + b
			counter += 1

	def test_generator(self):
		f = self.fibonacci(10)  # f是一个迭代器，由生成器返回生成
		while True:
			try:
				print(next(f))  # send(msg)与next()返回的是下一个yield表达式的参数
			except StopIteration:
				return


class PythonItertools(unittest.TestCase):
	""" itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算
	无穷循环器: count(), cycle(), repeat() """

	def test_count(self):
		print('module itertools: ')
		print(dir(itertools))

		for c in itertools.count(5, 2):  # 从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
			print(c)
			if c > 10:
				break

	def test_cycle(self):
		cs = itertools.cycle('ABC')  # cycle()会把传入的一个序列无限重复下去
		times = 0
		for c in cs:
			times += 1
			if times > 5:
				break
			print(c)

	def test_repeat(self):
		it = itertools.repeat('L', 3)  # repeat()把一个元素无限重复下去，第二个参数就可以限定重复次数
		self.assertEqual(list(it), ['L', 'L', 'L'])

	'''对于无限迭代, 可以通过takewhile()
	等函数根据条件判断来截取出一个有限的序列'''
	def test_takewhile(self):
		naturals = itertools.count(1)
		ns = itertools.takewhile(lambda x: x < 5, naturals)  # 当函数返回True时，收集元素到循环器。一旦函数返回False，则停止
		self.assertEqual(list(ns), [1, 2, 3, 4])

	def test_dropwhile(self):
		it = itertools.dropwhile(lambda x: x < 5, [1, 3, 7, 1, 3])  # 当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器
		self.assertEqual(list(it), [7, 1, 3])

	''' 函数式工具: 这些函数接收函数作为参数，并将结果返回为一个循环器 '''
	def test_starmap(self):
		it = itertools.starmap(pow, [(1, 1), (2, 2), (3, 3)])  # pow将依次作用于表的每个tuple
		self.assertEqual(list(it), [1, 4, 27])

	''' chain()可以把一组迭代对象串联起来，形成一个更大的迭代器 '''
	def test_chain(self):
		it = itertools.chain('ABC', 'def')
		self.assertEqual(list(it), ['A', 'B', 'C', 'd', 'e', 'f'])

	''' 多个循环器集合的笛卡尔积。相当于嵌套循环 '''
	def test_product(self):
		it = itertools.product('ab', [1, 2])
		self.assertEqual(list(it), [('a', 1), ('a', 2), ('b', 1), ('b', 2)])

	''' 从'abc'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器 '''
	def test_combinations(self):
		it = itertools.combinations('abc', 2)
		self.assertEqual(list(it), [('a', 'b'), ('a', 'c'), ('b', 'c')])

	''' 把迭代器中相邻的重复元素挑出来放在一起 '''
	def test_groupby(self):
		s = sorted('cBAaAbccC', key=lambda a: a.upper())  # 分组之前需要使用sorted()对原循环器的元素，根据key函数进行排序，让同组元素先在位置上靠拢
		for key, values in itertools.groupby(s, lambda a: a.upper()):  # 忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
			print(key, list(values))

	''' 根据[1, 0, 1, 0, 0, 1]的真假值情况，选择第一个参数'ABCD'中的元素。P, t, n '''
	def test_compress(self):
		it = itertools.compress('Python', [1, 0, 1, 0, 0, 1])
		self.assertEqual(list(it), ['P', 't', 'n'])

	''' 类似于slice()函数，只是返回的是一个循环器 '''
	def test_islice(self):
		it = itertools.islice('Python', 3)
		self.assertEqual(list(it), ['P', 'y', 't'])


if __name__ == '__main__':
	unittest.main()
