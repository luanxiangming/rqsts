import unittest
from collections import deque


class PythonLists(unittest.TestCase):
	def setUp(self):
		self.list1 = ['Google', 'Runoob', 1997, 2000]
		self.list2 = ['test']
		self.list3 = ['Google', 'Runoob', 'Zoo', 'Carpenter']

	def tearDown(self):
		self.list1, self.list2, self.list3 = [], [], []

	def test_update(self):
		self.list1[2] = 2017
		self.assertEqual(self.list1[2], 2017)

	def test_del(self):
		del self.list1[-1]
		self.assertEqual(len(self.list1), 3)

	def test_operations(self):
		self.assertEqual(self.list1 + self.list2, ['Google', 'Runoob', 1997, 2000, 'test'])
		self.assertEqual(self.list2 * 3, ['test', 'test', 'test'])

	def test_functions(self):
		self.assertEqual(len(self.list1), 4)
		self.assertEqual(max(self.list3), 'Zoo')
		self.assertEqual(min(self.list3), 'Carpenter')
		str = 'Hello World'
		self.assertEqual(list(str), ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'])  # 将元组转换为列表

	def test_methods(self):
		self.list1.append('test')
		self.assertEqual(self.list1[-1], 'test')

		self.list2.extend(list(range(3)))  # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
		self.assertEqual(self.list2, ['test', 0, 1, 2])

		self.assertEqual(self.list1.count(1997), 1)
		self.assertEqual(self.list1.index('Runoob'), 1)

		self.list3.insert(1, 'Baidu')
		self.assertEqual(self.list3, ['Google', 'Baidu', 'Runoob', 'Zoo', 'Carpenter'])

		self.list3.pop()
		self.assertEqual(self.list3, ['Google', 'Baidu', 'Runoob', 'Zoo'])  # 用于移除列表中的一个元素（默认最后一个元素）,并且返回该元素的值
		self.list3.pop(0)
		self.assertEqual(self.list3, ['Baidu', 'Runoob', 'Zoo'])

		self.list3.remove('Baidu')  # 用于移除列表中某个值的第一个匹配项
		self.assertEqual(self.list3, ['Runoob', 'Zoo'])

		self.list2.reverse()  # 用于反向列表中元素
		self.assertEqual(self.list2, [2, 1, 0, 'test'])

		self.list3.sort()  # 用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
		self.assertEqual(self.list3, ['Runoob', 'Zoo'])

		self.list3.clear()  # 用于清空列表，类似于 del a[:]
		self.assertEqual(self.list3, [])

		list_ = self.list2.copy()  # 用于复制列表，类似于 a[:]
		self.assertEqual(self.list2, list_)

	def test_enumerate(self):
		""" 带索引位置的集合遍历 """
		for i, name in enumerate(self.list3):
			print(i, name)

	def test_deque(self):
		""" 双向队列数据结构 """
		print('module deque: ')
		print(dir(deque))

		deq = deque(self.list1)
		self.assertEqual(deq.pop(), 2000)
		self.assertEqual(deq.popleft(), 'Google')

		deq.append(2001)
		self.assertEqual(deq, deque(['Runoob', 1997, 2001]))
		deq.appendleft('Baidu')
		self.assertEqual(deq, deque(['Baidu', 'Runoob', 1997, 2001]))


if __name__ == '__main__':
	unittest.main()
