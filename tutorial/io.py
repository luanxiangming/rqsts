import math
import pickle
import pprint
import unittest


class PythonIO(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	'''
	str()： 函数返回一个用户易读的表达形式
	repr()： 产生一个解释器易读的表达形式
	'''

	def test_repr(self):
		print('\n')
		print('result: ' + repr(1 / 7))
		print(str('Hello, Python\n'))
		print(repr('Hello, Python\n'))  # repr() 函数可以转义字符串中的特殊字符
		print(repr((100, 1.0, ('Hi', '100'))))  # repr() 的参数可以是 Python 的任何对象

	def test_square_cube(self):
		for x in range(1, 10):
			print(repr(x).rjust(2), repr(x ** 2).rjust(3), repr(x ** 3).zfill(4))

	def test_format(self):
		print('{} site: {}'.format('google', 'www.google.com'))  # 括号及其里面的字符(称作格式化字段)将会被format() 中的参数替换
		print('{1} site: {2}'.format('baidu', 'google', 'www.google.com'))  # 在括号中的数字用于指向传入对象在format() 中的位置
		print('{name} site: {site}'.format(name='google', site='www.google.com'))  # 关键字参数的值会指向使用该名字的参数
		print('PI约等于: {!r}'.format(math.pi))  # '!a'(使用 ascii()),'!s' (使用 str())和'!r'(使用 repr()) 可以用于在格式化某个值之前对其进行转化
		print('PI约等于: {:.3f}'.format(math.pi))  # 可选项 ':' 和格式标识符可以跟着字段名, 将 Pi 保留到小数点后三位
		print('PI约等于: %5.4f' % math.pi)  # 这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format()

		print('\n')
		for x in range(1, 9):
			print('{0:2} {1:3} {2:4}'.format(x, x ** 2, x ** 3))  # 在':'后传入一个整数, 可以保证该域至少有这么多的宽度

	'''
	r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
	rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
	r+	打开一个文件用于读写。文件指针将会放在文件的开头。
	rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
	w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
	wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
	w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
	wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
	a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
	a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
	ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
	'''

	def test_file_write(self):
		f = open('tmp/foo.txt', 'w')
		num = f.write('A: Python is great computer language.\nB: Yes, indeed.\n')  # 将string写入到文件中,然后返回写入的字符数
		print('file_write: ' + str(num))
		f.close()

		f = open('tmp/foo.txt', 'a')
		content = ('www.google.com', 7)
		f.write(str(content))  # 如果要写入一些不是字符串的东西, 那么将需要先进行转换
		f.close()

	def test_file_read(self):
		f = open('tmp/foo.txt', 'r')
		content = f.read()  # size是一个可选的数字类型的参数。 当size被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回
		print(content)
		f.close()

		f = open('tmp/foo.txt', 'r')
		line = f.readline()  # 从文件中读取单独的一行。换行符为 '\n'。如果返回一个空字符串, 说明已经已经读取到最后一行
		print('line: ' + line)
		f.close()

		f = open('tmp/foo.txt', 'r')
		lines = f.readlines()
		for line in lines:
			print(line)
		f.close()

	def test_file_tell(self):
		f = open('tmp/foo.txt', 'r')
		print('file_tell_begin: ' + str(f.tell()))  # 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
		f.readlines()
		print('file_tell_end: ' + str(f.tell()))
		f.close()

	def test_file_seek(self):
		f = open('tmp/foo.txt', 'rb+')
		f.write(b'0123456789abcdef')
		print('file_seek_1: ' + str(f.tell()))
		f.seek(5, 0)  # 从起始位置即文件首行首字符开始移动5个字符
		print('file_seek_2: ' + str(f.tell()))
		print(f.read(2))  # 调用f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回
		print('file_seek_3: ' + str(f.tell()))
		f.seek(2, 1)  # 从当前位置往后移动2个字符
		print('file_seek_4: ' + str(f.tell()))
		f.seek(-3, 2)  # 从文件的结尾往前移动3个字符
		print('file_seek_5: ' + str(f.tell()))
		f.close()

	"""
	python的pickle模块实现了基本的数据序列和反序列化。
	通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
	通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
	"""

	def test_pickle_dump(self):
		# 使用pickle模块将数据对象保存到文件
		# 基本接口: pickle.dump(obj, file, [,protocol])
		data1 = {
			"a": [1, 2.0, 3, 4 + 6j],
			"b": ('string', u'Unicode string'),
			"c": None
		}

		selfref_list = [1, 2, 3]
		with open('tmp/data.pkl', 'wb') as f:
			pickle.dump(data1, f)  # Pickle dictionary using protocol 0
			pickle.dump(selfref_list, f, -1)  # Pickle list using the highest protocol available

	def test_pickle_load(self):
		# 使用pickle模块从文件中重构python对象
		# 基本接口: x = pickle.load(file)
		with open('tmp/data.pkl', 'rb') as f:
			content = pickle.load(f)
			pprint.pprint(content)


if __name__ == '__main__':
	unittest.main()
