from collections import *


def collections_nametuple():
	"""
	namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
	"""
	Point = namedtuple('Point', ['x', 'y'])
	p = Point(1, 2)
	print('p.x: ' + str(p.x))
	print('isInstance(p, Point): ' + str(isinstance(p, Point)))
	print('isInstance(p, tuple): ' + str(isinstance(p, tuple)))  # Point对象是tuple的一种子类

	Circle = namedtuple('Circle', ['x', 'y', 'r'])
	circle = Circle(2, 2, 1)
	print('circle.r: ' + str(circle.r))


def collections_ordereddict():
	dt = {'a': 1, 'c': 2, 'b': 3}
	for k, v in dt.items():
		print(k + ': ' + str(v))
	print('\n')

	# sort by key
	od = OrderedDict(sorted(dt.items(), key=lambda t: t[0]))
	for x, y in od.items():
		print(x + ': ' + str(y))
	print('\n')

	# sort by value
	od = OrderedDict(sorted(dt.items(), key=lambda t: t[1]))
	for i, j in od.items():
		print(i + ': ' + str(j))
	print('\n')


def collections_counter():
	"""
	Counter是一个简单的计数器
	实际上是dict的一个子类，结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次
	"""
	c = Counter()
	for i in 'Programming':
		c[i] += 1
	print(c)
	for i, c in c.most_common():  # most_common这个列表中的每个元素都返回一个元祖，一组有序唯一值
		print(i, c)
	print('\n')


def collections_defaultdict():
	"""
	注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
	"""
	dd = defaultdict(lambda: 'N/A')
	dd[0] = 1
	print(dd[0])  # 存在
	print(dd[1])  # 不存在，返回默认值
	print(dd[2])  # 不存在，返回默认值


collections_nametuple()
collections_ordereddict()
collections_counter()
collections_defaultdict()
