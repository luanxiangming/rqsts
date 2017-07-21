from enum import Enum


class Test:
	# 类的实例化操作会自动调用 __init__() 构造方法
	def __init__(self):
		self.data = 'Implicit'

	def print_self(self):
		print(self)  # self代表类的实例，代表当前对象的地址, 而非类
		print(self.data)
		print(dir(self))
		print('class: ' + str(self.__class__))  # 指向类
		print('module: ' + str(self.__module__))
		print('dict: ' + str(self.__dict__))
		print('weakref: ' + str(self.__weakref__))


t = Test()
t.print_self()


class People:
	# 定义基本属性
	name, age = '', 0
	__weight = 0  # 定义私有属性,类外部无法直接进行访问

	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w

	def __repr__(self):
		return "%s-%s-%s-%s" % (self.__class__, self.name, self.age, self.__weight)

	def __str__(self):
		return "%s: %s" % (self.name, self.age)

	def speak(self):  # 覆写父类的方法
		print('\nMy name is {} and {} years old, weight-{}'.format(self.name, self.age, self.__weight))


p = People('Alice', 10, 50)
p.speak()


class Speaker:
	def __init__(self, t, n):
		self.topic = t
		self.name = n

	def speak(self):
		print("My name is {} and today's topic is {}".format(self.name, self.topic))


s = Speaker("Economic", 'Hayek')
s.speak()


class Student(People):
	""" 单继承 """
	grade = ''

	def __init__(self, n, a, w, g):
		People.__init__(self, n, a, w)  # 调用父类的构函
		self.grade = g

	def speak(self):
		print('My name is {} and {} years old with {} grade.'.format(self.name, self.age, self.grade))


s = Student('John', 12, 60, 'fifth')
s.speak()


class Sample(Speaker, Student):
	""" 多继承 """

	def __init__(self, t, n, a, w, g):
		Speaker.__init__(self, t, n)
		Student.__init__(self, n, a, w, g)


sample = Sample('Python', 'Lewis', '20', 50, '10th')
sample.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


class Vector:
	"""类的专有方法：
	__init__ : 构造函数，在生成对象时调用
	__del__ : 析构函数，释放对象时使用
	__repr__ : 打印，转换
	__setitem__ : 按照索引赋值
	__getitem__: 按照索引获取值
	__len__: 获得长度
	__cmp__: 比较运算
	__call__: 函数调用
	__add__: 加运算
	__sub__: 减运算
	__mul__: 乘运算
	__div__: 除运算
	__mod__: 求余运算
	__pow__: 称方
	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		""" 如果没有提供 __str__，缺省使用 repr() 的结果, 优先使用 str() 的结果"""
		return 'Vector: ({}, {})'.format(self.x, self.y)

	def __add__(self, other):
		""" 可以对类的专有方法进行重载 """
		return Vector(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return Vector(self.x * other.x, self.y * other.y)

	def __len__(self):
		return self.x + self.y

	def set(this, x, y):
		""" self 并不是关键字，甚至可以用其它名字替代，比如 this """
		this.x = x
		this.y = y


v1 = Vector(1, 2)
v2 = Vector(3, 4)

# set(...) 其实只是一个语法糖，你也可以写成 Vector.set(v, ...)，这样就能明显看出 v 就是 self 参数了
v1.set(5, 5)
Vector.set(v2, 10, 10)
print('v1+v2:', v1 + v2)
print('v1*v2: ', v1 * v2)
print('len(v1), len(v2): ', len(v1), len(v2))


class Animal(Enum):
	""" Python没有enum块，但它有Enum模块
	Enum创建了一个固定数量的类的集合而不是类属性
	"""
	cat = 0
	dog = 1
	mouse = 2
	snake = 3


print(Animal.cat)
print(Animal.cat.value)
print(Animal(2))
print(Animal['dog'])
