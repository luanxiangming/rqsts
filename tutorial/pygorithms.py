import unittest
from pygorithm.sorting import bubble_sort
from pygorithm.searching import binary_search, linear_search


class PythonPygorithm(unittest.TestCase):
	def setUp(self):
		self.list1 = [12, 4, 2, 14, 3, 7, 5]

	def tearDown(self):
		self.list1 = []

	def test_bubble_sort(self):
		""" 对列表进行排序 """
		print("module pygorithm bubble_sort:")
		print(dir(bubble_sort))

		bubble_sort.sort(self.list1)
		self.assertEqual(self.list1, [2, 3, 4, 5, 7, 12, 14])

	def test_get_code(self):
		""" 获取算法对应的代码 """
		print(bubble_sort.get_code())

	def test_time_complexity(self):
		""" 获取一个算法的时间复杂度 """
		print(bubble_sort.time_complexities())

	def test_binary_search(self):
		print("module pygorithm binary_search")
		print(dir(binary_search))

		bubble_sort.sort(self.list1)  # pre-requisite for binary search is that the list should be sorted
		self.assertEqual(binary_search.search(self.list1, 7), 4)

	def test_linear_search(self):
		print("module pygorithm linear_search")
		print(dir(linear_search))

		self.assertEqual(linear_search.search(self.list1, 7), 5)


if __name__ == '__main__':
	unittest.main()
