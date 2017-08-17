class Goods(object):
	""" 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
	由于新式类中具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
	"""

	def __init__(self):
		self.original_price = 100
		self.discount = 0.8

	@property
	def price(self):
		return self.original_price * self.discount

	@price.setter
	def price(self, value):
		self.original_price = value

	@price.deleter
	def price(self):
		del self.original_price

	"""由于静态字段方式创建属性具有三种访问方式，
	我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
	"""

	def get_price(self):
		return self.original_price * self.discount

	def set_price(self, value):
		self.original_price = value

	def del_price(self):
		del self.original_price

	PRICE = property(get_price, set_price, del_price, '价格属性描述..')


goods = Goods()

goods.price = 1000
print(goods.price)
del goods.price

goods.PRICE = 2000  # 修改商品原价
print(goods.PRICE)  # 获取商品价格
del goods.PRICE  # 删除商品原价

""" 获取类的成员，即：静态字段、方法 """
print(Goods.__dict__)
print(goods.__dict__)


class Foo:
	""" 当使用静态字段的方式创建属性时，经典类和新式类无区别 """

	def get_bar(self):
		return 'bar'

	def set_bar(self, value):
		return 'set_bar: ' + value

	def del_bar(self):
		return 'del_bar'

	BAR = property(get_bar, set_bar, del_bar, 'description')


foo = Foo()
print(foo.BAR)  # 自动调用第一个参数中定义的方法：get_bar
foo.BAR = 'OL'  # 自动调用第二个参数中定义的方法：set_bar方法，并将“OL”当作参数传入
del foo.BAR  # 自动调用第三个参数中定义的方法：del_bar方法
foo.BAR.__doc__
