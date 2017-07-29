import unittest


class PythonTuples(unittest.TestCase):
	def setUp(self):
		self.tup1 = ('Google', 'Runoob', 1997, 2000)
		self.tup2 = (1, 2, 3, 4, 5, 6, 7)
		self.tup3 = 'Google', 'Runoob', 1997, 2000

	def tearDown(self):
		self.tup1, self.tup2, self.tup3 = (), (), ()

	def test_create(self):
		self.assertEqual(self.tup1, self.tup3)

	def test_convert(self):
		self.assertEqual(tuple([1, 2, 3, 4, 5, 6, 7]), self.tup2)

	def test_update(self):
		tup = self.tup1 + self.tup2
		self.assertEqual(tup, ('Google', 'Runoob', 1997, 2000, 1, 2, 3, 4, 5, 6, 7))

	def test_functions(self):
		self.assertEqual(len(self.tup1), 4)
		self.assertEqual(max(self.tup2), 7)
		self.assertEqual(min(self.tup2), 1)

		tup = tuple(['Google', 'Taobao', 'Runoob', 'Baidu'])  # 将列表转换为元组
		self.assertEqual(tup, ('Google', 'Taobao', 'Runoob', 'Baidu'))


if __name__ == '__main__':
	unittest.main()
