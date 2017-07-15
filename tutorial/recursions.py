import inspect, sys

print(inspect.stack())


def a():
	"""
	当inspect.stack()第一次被调用时，一个栈帧加到了堆栈中。再次调用，堆栈中就有两个栈帧了。
	"""
	print(inspect.stack())


def factorial_recursion(n):
	if n == 1:
		return 1
	else:
		result = n * factorial_recursion(n - 1)
		return result


def factorial_recursion_new(n, result):
	"""
	一系列扁平的factorial()调用，状态保存在变量result中，而不是由解释器来保存
	在“尾递归”语言中，以这种方式定义的递归过程可以被解释器解释为迭代，从而不会带来递归的缺点。
	用这种优雅的递归过程，能使你获得和迭代一样的性能优势。解释器知道不需要在堆栈上创建更多的栈帧，从而抛弃创建栈帧的方式。
	"""
	if n == 1:
		return result
	else:
		return factorial_recursion_new(n - 1, n * result)


def factorial_iteration(n):
	"""
	栈帧产生系统开销，所以在命令式语言中，递归是内存密集型的操作。相比下面的使用迭代方式获取阶乘的函数
	"""
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result


a()

print(factorial_recursion(20))
print(factorial_iteration(20))
print(factorial_recursion_new(20, 1))

"""
栈帧消耗内存，而一个Python进程只能分配到有限的内存。
如果堆栈包含太多的栈帧，进程会耗尽所分配的内存，或者堆栈可能扩展到没有分配给该进程的内存空间而导致堆栈溢出。
为了防止出现这样的问题，解释器会设置一个最大递归数的限制，可以通过调用sys.getrecursionlimit()来查看这个限制
"""
print(sys.getrecursionlimit())
