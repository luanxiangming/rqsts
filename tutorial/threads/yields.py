def h():
	print('*****生成器启动*****')
	m = yield 5  # Fighting!
	print(m)
	d = yield 12
	print('We are together!')


c = h()
next(c)  # 相当于c.send(None)，用来启动生成器
c.send('Fighting!')  # (yield 5)表达式被赋予了'Fighting!'


def f():
	print('\nstart')
	a = yield 1
	print(a)
	print('middle....')
	b = yield 2  # 2这个值只是迭代值，调用next时候返回的值
	print(b)  # 传入的参数是给当前yield的，也就是yield 2，因为当前函数走到了yield 2，所以传入的参数没有给yield 1
	print('next')
	c = yield 3
	print(c)


a = f()
print('next()返回yield 1的参数: ' + str(next(a)))  # send(msg)与next()返回的是下一个yield表达式的参数
print('next()返回yield 2的参数: ' + str(next(a)))
a.send('为yield 2赋值')


def odd_numbers():
	n = 1
	while True:
		yield n
		n += 2


for x in odd_numbers():
	print(x)
	if x > 10:
		break
