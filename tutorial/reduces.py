import unittest
from functools import reduce


class PythonReduce(unittest.TestCase):
	"""reduce函数即为化简
	它是这样一个过程：每次迭代，将上一次的迭代结果（第一次时为init的元素，如没有init则为seq的第一个元素）与下一个元素一同执行一个二元的func函数。
	在reduce函数中，init是可选的，如果使用，则作为第一次迭代的第一个元素使用。
	"""

	def test_reduce(self):
		reduced = reduce(lambda x, y: x + y, range(5))
		self.assertEqual(reduced, 0 + 1 + 2 + 3 + 4)

	def test_factorial(self):
		reduced = reduce(lambda x, y: x * y, range(1, 6))
		reduced_with_init = reduce(lambda x, y: x * y, range(1, 6), 2)

		self.assertEqual(reduced, 1 * 2 * 3 * 4 * 5)
		self.assertEqual(reduced_with_init, 2 * 1 * 2 * 3 * 4 * 5)


if __name__ == "__main__":
	unittest.main()
