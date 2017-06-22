import unittest


class PythonMaps(unittest.TestCase):
	""" map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回 """

	@staticmethod
	def add100(x):
		return x+100

	@staticmethod
	def abc(a, b, c):
		return a*100+b*10+c

	def test_single_arg(self):
		""" 对可迭代函数'iterable'中的每一个元素应用‘function’方法
		map(f, iterable)基本上等于：[f(x) for x in iterable]
		"""
		map_ = map(self.add100, range(5))
		self.assertEqual(list(map_), [100, 101, 102, 103, 104])
		self.assertEqual([self.add100(x) for x in range(5)], [100, 101, 102, 103, 104])

	def test_multiple_args(self):
		""" 对每个可迭代参数中的元素‘并行’应用‘function’ """
		map_ = map(self.abc, [1, 2, 3], [4, 5, 6], [7, 8, 9])
		self.assertEqual(list(map_), [147, 258, 369])


if __name__ == '__main__':
	unittest.main()
