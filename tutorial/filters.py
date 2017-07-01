import unittest


class PythonFilter(unittest.TestCase):
	"""filter()函数用于过滤序列
	和map()类似，filter()也接收一个函数和一个序列。
	和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
	"""

	@staticmethod
	def is_even(num):
		return num % 2 == 0

	@staticmethod
	def is_not_prime(num):
		for i in range(2, num):
			if num % i == 0:
				return True
		else:
			return False

	def test_filter(self):
		filter_list = filter(self.is_even, range(10))
		self.assertEqual(list(filter_list), [0, 2, 4, 6, 8])

	def test_filter_prime(self):
		filter_list = filter(self.is_not_prime, range(100))
		print(list(filter_list))


if __name__ == "__main__":
	unittest.main()
