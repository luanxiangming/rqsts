import timeit


def decorate(function):
	cache = {}

	def wrapper(*args):
		if args not in cache:
			cache[args] = function(*args)
		return cache[args]

	return wrapper


@decorate
def fibonacci(n):
	if n < 2:
		return 1
	else:
		return fibonacci(n - 2) + fibonacci(n - 1)


t = timeit.timeit('fibonacci(10)', 'from __main__ import fibonacci')
print(t)
