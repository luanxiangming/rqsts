import unittest
from collections import deque


class PythonDatas(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	'''
	将列表当做堆栈使用
	列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）
	用append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
	'''

	def test_stack(self):
		stack = [3, 4, 5]
		stack.append(6);
		stack.append(7)
		self.assertEqual(stack, [3, 4, 5, 6, 7])
		stack.pop();
		stack.pop();
		self.assertEqual(stack, [3, 4, 5])

	'''
	将列表当作队列使用
	也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高
	在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）
	'''

	def test_queue(self):
		queue = deque([3, 4, 5])
		queue.append(6);
		queue.append(7)
		self.assertEqual(queue, deque([3, 4, 5, 6, 7]))
		queue.popleft();
		queue.popleft()
		self.assertEqual(queue, deque([5, 6, 7]))

	# 列表推导式
	def test_list_comprehension(self):
		vec = [2, 4, 6]
		self.assertEqual([x * 3 for x in vec], [6, 12, 18])
		self.assertEqual([x * 3 for x in vec if x < 5], [6, 12])  # 可以用 if 子句作为过滤器
		self.assertEqual([[x, x ** 2] for x in vec], [[2, 4], [4, 16], [6, 36]])

		freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
		self.assertEqual([x.strip() for x in freshfruit], ['banana', 'loganberry', 'passion fruit'])  # 对序列里每一个元素逐个调用某方法

		vec1 = [2, 4, 6]
		vec2 = [4, 3, -9]
		self.assertEqual([x * y for x in vec1 for y in vec2], [8, 6, -18, 16, 12, -36, 24, 18, -54])
		self.assertEqual([vec1[i] * vec2[i] for i in range(len(vec1))], [8, 12, -54])

		# 将3X4的矩阵列表转换为4X3列表
		maxtrix = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12],
		]
		print([[row[i] for row in maxtrix] for i in range(4)])

		# 方法二
		transpose = []
		for i in range(4):
			transpose.append([row[i] for row in maxtrix])
		print(transpose)

	# 遍历技巧
	def test_zip(self):
		questions = ['name', 'quest', 'favorite color']
		answers = ['lancelot', 'the holy grail', 'blue']
		for k, v in zip(questions, answers):  # 同时遍历两个或更多的序列，可以使用 zip() 组合
			print(k + ": " + v)

		for i in reversed(range(5)):
			print(i)

		basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
		for i in sorted(set(basket)):  # 按顺序遍历一个序列，使用sorted() 函数返回一个已排序的序列，并不修改原值：
			print(i)


if __name__ == '__main__':
	unittest.main()
