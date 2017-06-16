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

	def speak(self):  # 覆写父类的方法
		print('\nMy name is {} and {} years old'.format(self.name, self.age))


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

''' 单继承 '''


class Student(People):
	grade = ''

	def __init__(self, n, a, w, g):
		People.__init__(self, n, a, w)  # 调用父类的构函
		self.grade = g

	def speak(self):
		print('My name is {} and {} years old with {} grade.'.format(self.name, self.age, self.grade))


s = Student('John', 12, 60, 'fifth')
s.speak()

''' 多继承 '''


class Sample(Speaker, Student):
	def __init__(self, t, n, a, w, g):
		Speaker.__init__(self, t, n)
		Student.__init__(self, n, a, w, g)


sample = Sample('Python', 'Lewis', '20', 50, '10th')
sample.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

'''类的专有方法：
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
'''


class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return ('Vector: ({}, {})'.format(self.x, self.y))

	# 可以对类的专有方法进行重载
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y)

	def __mul__(self, other):
		return Vector(self.x * other.x, self.y * other.y)

	def __len__(self):
		return (self.x + self.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 * v2)
print(len(v1), len(v2))
