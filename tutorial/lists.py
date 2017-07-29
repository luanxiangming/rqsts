import bisect
import unittest
from collections import deque


class PythonLists(unittest.TestCase):
	def setUp(self):
		self.list1 = ['Google', 'Runoob', 1997, 2000]
		self.list2 = ['test']
		self.list3 = ['Google', 'Runoob', 'Zoo', 'Carpenter']
		self.list4 = [4, 2, 9, 7]

	def tearDown(self):
		self.list1, self.list2, self.list3, self.list4 = [], [], [], []

	def test_update(self):
		self.list1[2] = 2017
		self.assertEqual(self.list1[2], 2017)

	def test_del(self):
		del self.list1[-1]
		self.assertEqual(len(self.list1), 3)

	def test_operations(self):
		""" List concatenation using '+' is expensive since
		a new list must be created and objects copied
		over. Thus, extend() is preferable.
		"""
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

		self.list3.insert(1, 'Baidu')  # Insert is computationally expensive compared with append
		self.assertEqual(self.list3, ['Google', 'Baidu', 'Runoob', 'Zoo', 'Carpenter'])

		self.list3.pop()
		self.assertEqual(self.list3, ['Google', 'Baidu', 'Runoob', 'Zoo'])  # 用于移除列表中的一个元素（默认最后一个元素）,并且返回该元素的值
		self.list3.pop(0)
		self.assertEqual(self.list3, ['Baidu', 'Runoob', 'Zoo'])

		self.list3.remove('Baidu')  # 用于移除列表中某个值的第一个匹配项
		self.assertEqual(self.list3, ['Runoob', 'Zoo'])

		self.list2.reverse()  # 用于反向列表中元素
		self.assertEqual(self.list2, [2, 1, 0, 'test'])
		self.assertEqual(self.list2[::-1], ['test', 0, 1, 2])  # another reverse

		self.list3.sort()  # 用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
		self.assertEqual(self.list3, ['Runoob', 'Zoo'])
		self.list3.sort(key=len)
		self.assertEqual(self.list3, ['Zoo', 'Runoob'])

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

	def test_bisect(self):
		""" bisect module functions do not
		check whether the list is sorted, doing so would
		be computationally expensive. Thus, using them
		in an unsorted list will succeed without error but
		may lead to incorrect results.
		"""
		self.list4.sort()  # 使用bisect模块的函数前先确保操作的列表是已排序的
		self.assertEqual(self.list4, [2, 4, 7, 9])

		bisect.insort(self.list4, 8)
		self.assertEqual(self.list4, [2, 4, 7, 8, 9])

		# 查找该数值将会插入的位置并返回，而不会插入
		self.assertEqual(bisect.bisect(self.list4, 5), 2)
		self.assertEqual(self.list4, [2, 4, 7, 8, 9])

		# 处理将会插入重复数值的情况，返回将会插入的位置
		self.assertEqual(bisect.bisect_left(self.list4, 4), 1)
		self.assertEqual(bisect.bisect_right(self.list4, 4), 2)

		# 对应的插入函数是 insort_left  和 insort_right
		bisect.insort_left(self.list4, 4)
		self.assertEqual(self.list4, [2, 4, 4, 7, 8, 9])
		bisect.insort_right(self.list4, 7)
		self.assertEqual(self.list4, [2, 4, 4, 7, 7, 8, 9])


if __name__ == '__main__':
	unittest.main()
