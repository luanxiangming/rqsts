import unittest


class PythonSet(unittest.TestCase):
	"""
	A set is an unordered collection of UNIQUE elements.
	You can think of them like dicts but keys only
	"""

	def setUp(self):
		self.set1 = {3, 6, 3, 4}
		self.set2 = {3, 6}
		self.set3 = {3, 6, 4}
		self.set4 = {5, 6}
		self.set5 = {(1, 3), (2, 4)}

	def test_subset_superset(self):
		self.assertTrue(self.set2.issubset(self.set1))
		self.assertTrue(self.set1.issuperset(self.set2))

	def test_equal(self):
		self.assertTrue(self.set1 == self.set3)

	def test_operation(self):
		self.assertEqual(self.set2 | self.set4, {3, 5, 6})  # Union(aka 'or')
		self.assertEqual(self.set2 & self.set4, {6})  # Intersection (aka 'and')
		self.assertEqual(self.set2 - self.set4, {3})  # Difference
		self.assertEqual(self.set2 ^ self.set4, {3, 5})  # Symmetric Difference (aka 'xor')

	def test_set_comprehension(self):
		s = {x for x in self.set4}
		self.assertEqual(s, {5, 6})
		ss = {x for i in self.set5 for x in i if x > 2}
		self.assertEqual(ss, {3, 4})


if __name__ == '__main__':
	unittest.main()
