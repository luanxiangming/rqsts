def repeat(name, count):
	for i in range(count):
		print(name)


def packing():
	""" *运算符，被称为拆包或splat运算符，允许非常方便的从列表或元组到独立的变量或参数的转换，反之亦可 """
	a, *b, c = [2, 7, 2, 5, 6]
	print(a)
	print(b)
	print(c)


def unpacking():
	""" 当你的函数的参数已经在列表或元组中，可对其拆包。如果是列表你可以用*args来拆包，如果是字典就用**kwargs """
	args1 = ['Python', 5]
	repeat(*args1)  # Call function using a list of argument

	args2 = {'count': 3, 'name': 'Java'}
	repeat(**args2)  # Call function using a dict of keyword argument


def f(*args, **kwargs):
	""" 反过来也是可以的，你可以定义一个函数，将单个tuple里的所有参数和单个dict里的所有的关键字参数组包 """
	print('args: ', args)
	print('keyword args: ', kwargs.items())


packing()
unpacking()

f(1, 4, 9, foo=1, bar=2)
