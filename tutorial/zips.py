import unittest


class PythonZip(unittest.TestCase):
	"""
	zip()是Python的一个内建函数
	它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）。
	若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。利用*号操作符，可以将list unzip（解压）
	"""

	def test_zip_normal(self):
		list1 = [1, 2, 3]
		list2 = [5, 6, 7]
		self.assertEqual(list(zip(list1, list2)), [(1, 5), (2, 6), (3, 7)])

	def test_zip_diff_length(self):
		list1 = [1, 2, 3]
		list2 = [5, 6]
		self.assertEqual(list(zip(list1, list2)), [(1, 5), (2, 6)])

	def test_zip_empty_seq(self):
		self.assertEqual(list(zip()), [])

	def test_zip_single_seq(self):
		self.assertEqual(list(zip([1, 2, 3])), [(1,), (2,), (3,)])


if __name__ == "__main__":
	unittest.main()
