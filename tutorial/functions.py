import functools


def print_info(arg1, *argtuple):
	print(arg1)
	for arg in argtuple:
		print(arg)


def test_mutable_args():
	print_info(10, 'ag1', 'ag2')


def test_lambda():
	sum = lambda arg1, arg2: arg1 + arg2
	print('sum: ', sum)
	print('sum(1, 10): ', sum(1, 10))

	# 排序函数sorted()可以接收一个函数作为参数
	list_ = [-2, -4, -3, 1]
	print(list(sorted(list_, key=lambda x: abs(x))))
	list_ = [['a', 85], ['b', 70], ['d', 90], ['e', 100]]
	print(list(sorted(list_, key=lambda x: x[1], reverse=True)))


num = 1


def test_global_var():
	""" 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了 """
	global num  # 需要使用 global 关键字声明
	print('global: ' + str(num))
	num = 100
	print('local: ' + str(num))


def test_outer():
	""" 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了 """
	num = 200

	def test_inner():
		nonlocal num  # nonlocal关键字声明
		num = 300
		print('inner: ' + str(num))

	test_inner()
	print('outer: ' + str(num))


def cache(function):
	""" 装饰器是一个接受函数作为参数并返回函数的函数
	cache函数用作装饰器来记住已经计算出的斐波那契数 """
	cached_values = {}  # Contains already computed values

	def wrapping_function(*args):
		if args not in cached_values:
			# Call the function only if we've not already done it for those parameters
			cached_values[args] = function(*args)
		return cached_values[args]

	return wrapping_function


@cache
@functools.lru_cache(None)
def fibonacci(n):
	""" functools模块提供了几个装饰器，例如lru_cache，它可以实现我们刚刚做的：存储。
	当使用相同的参数调用给定的函数时，它可以保存最近的调用来节省时间 """
	x, y = 0, 1
	for i in range(n):
		x, y = y, x + y
	return x


def test_cache():
	print([fibonacci(n) for n in range(10)])


test_lambda()
test_outer()
test_global_var()
test_mutable_args()
test_cache()
