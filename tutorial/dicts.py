import unittest

class PythonDicts(unittest.TestCase):
	def setUp(self):
		self.dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
		self.dict2 = {'Name': 'Python'}

	def tearDown(self):
		self.dict1 = {}

	def test_update(self):
		self.dict1['Age'] = 17; self.dict1['School'] = 'Harvard'
		self.assertEqual(self.dict1['Age'], 17); self.assertEqual(self.dict1['School'], 'Harvard')

	def test_del(self):
		del self.dict1['Class']
		self.assertEqual(self.dict1, {'Name': 'Runoob', 'Age': 7})

		self.dict1.clear()
		self.assertEqual(len(self.dict1), 0)

	def test_methods(self):
		# dict2是dict1的引用（别名），所以输出结果都是一致的，dict3父对象进行了深拷贝，不会随dict1修改而修改，子对象是浅拷贝所以随dict1的修改而修改
		dict2 = self.dict1
		dict3 = self.dict1.copy()
		self.dict1['Age'] = 8; self.dict1['Class'] = 'Second'
		self.assertEqual(self.dict1, {'Name': 'Runoob', 'Age': 8, 'Class': 'Second'})
		self.assertEqual(dict2, {'Name': 'Runoob', 'Age': 8, 'Class': 'Second'})
		self.assertEqual(dict3, {'Name': 'Runoob', 'Age': 7, 'Class': 'First'})

		# fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
		seq = ('name', 'age', 'sex')
		dict_ = dict.fromkeys(seq)
		self.assertEqual(dict_, {'name': None, 'age': None, 'sex': None})
		dict_ = dict.fromkeys(seq, 10)
		self.assertEqual(dict_, {'name': 10, 'age': 10, 'sex': 10})

		#返回指定键的值，如果值不在字典中返回默认值None
		self.assertEqual(self.dict2.get('Name'), 'Python'); self.assertEqual(self.dict2.get('Sex', 'male'), 'male') 
		# setdefault() 方法和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
		self.assertEqual(self.dict2.setdefault('Name'), 'Python'); self.assertEqual(self.dict2.setdefault('School', 'Harvard'), 'Harvard')
		self.assertTrue('Name' in self.dict2) #判断键是否存在于字典中
		print("Dict items: " + str(self.dict2.items())) #以列表返回可遍历的(键, 值) 元组数组
		print("Dict keys: " + str(self.dict2.keys())) #以列表返回一个字典所有的键
		print("Dict values: " + str(self.dict2.values())) #以列表返回字典中的所有值

		dict_ = {'nation': 'CN'}
		dict_.update(self.dict2) #把字典dict2的键/值对更新到dict_里
		self.assertEqual(dict_, {'Name': 'Python', 'School':'Harvard', 'nation': 'CN'})



if __name__ == '__main__':
	unittest.main()