import unittest
import sys


class PythonIterations(unittest.TestCase):
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
				print(next(f))
			except StopIteration:
				return


if __name__ == '__main__':
	unittest.main()
