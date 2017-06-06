
def print_info(arg1, *argtuple):
	print(arg1)
	for arg in argtuple:
		print(arg)	
def test_mutable_args():
	print_info(10, 'ag1', 'ag2')

def test_lambda():
	sum = lambda arg1, arg2 : arg1 + arg2
	# self.assertEqual(sum(10, 20), 30)
	print(sum)

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
num = 1
def test_global_var():
	global num # 需要使用 global 关键字声明
	print(num)
	num = 100
	print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def test_outer():
	num = '200'
	def test_inner():
		nonlocal num # nonlocal关键字声明
		num = '300'
		print('inner: ' + num)
	test_inner()
	print('outer: ' + num)

def main():
	test_outer()

if __name__ == '__main__':
	main()
