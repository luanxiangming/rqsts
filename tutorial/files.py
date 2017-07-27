import glob
import itertools
import pathlib

import os
import pickle
import unittest


class PythonFiles(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_file_close(self):
		pass

	def test_file_flush(self):
		pass

	def test_file_exists(self):
		# os.path.exists()方法，判断文件和文件夹是一样。
		self.assertTrue(os.path.exists('tmp'))
		self.assertTrue(os.path.exists('tmp/foo.txt'))
		# 只检查文件
		self.assertFalse(os.path.isfile('tmp'))
		self.assertTrue(os.path.isfile('tmp/foo.txt'))

	def test_file_access(self):
		""" 判断文件是否可做读写操作 """
		self.assertTrue(os.access('tmp', os.F_OK))  # 文件是否存在
		self.assertTrue(os.access('tmp/foo.txt', os.R_OK))  # 文件是否可读
		self.assertTrue(os.access('tmp/foo.txt', os.W_OK))  # 文件是否可写
		self.assertTrue(os.access('tmp/foo.txt', os.X_OK))  # 文件是否可执行

	def test_file_open(self):
		""" 可以在程序中直接使用open()方法来检查文件是否存在和可读写 """
		try:
			with open('tmp/foo1.txt') as f:
				print('Try to open %s' % f)
		except IOError:
			print('File cannot be accessed')

	def test_pathlib(self):
		""" 使用pathlib需要先使用文件路径来创建path对象。此路径可以是文件名或目录路径 """
		dir_path = pathlib.Path('tmp')
		self.assertTrue(dir_path.exists())  # 检查路径是否存在
		file_path = pathlib.Path('tmp/foo.txt')
		self.assertTrue(file_path.is_file())  # 检查路径是否是文件

	def test_fileno(self):
		""" 返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的I/O操作 """
		with open('tmp/foo.txt', 'r') as f:
			print(f.fileno())

	def test_fileisatty(self):
		""" 检测文件是否连接到一个终端设备 """
		with open('tmp/foo.txt', 'r') as f:
			self.assertFalse(f.isatty())

	def test_file_next(self):
		""" 函数 next() 通过迭代器调用 __next__() 方法返回下一项 """
		with open('tmp/foo.txt', 'r') as f:
			for row in range(2):
				print('Row {row}: {line}'.format(row=row, line=next(f)))

	def test_file_read(self):
		with open('tmp/foo.txt', 'r+') as f:
			print('All: ' + f.read())  # 从文件读取指定的字节数，如果未给定或为负则读取所有
			f.seek(0)
			print('First five: ' + f.read(5))

	def test_read_line(self):
		with open('tmp/foo.txt', 'r+') as f:
			self.assertEqual(f.readline(), 'A: Python is great computer language.\n')  # 从文件读取整行，包括 "\n" 字符
			self.assertEqual(f.readline(6), 'B: Yes')  # 如果指定了一个非负数的参数，则返回指定大小的字节数

	def test_read_lines(self):
		with open('tmp/foo.txt', 'r+') as f:
			print('打开文件：{}'.format(f.name))
			print(f.readlines())  # 读取所有行并返回列表

	def test_file_seek_tell(self):
		with open('tmp/foo.txt', 'r+') as f:
			print('Position1 before readline: ' + str(f.tell()))
			f.readline()
			print('Position2 after readline: ' + str(f.tell()))
			f.seek(5, 0)
			print('Position3 seek offset 5 from begenning: ' + str(f.tell()))
			print('Seek offset 5 from begenning: ' + f.readline())

	def test_truncate(self):
		with open('tmp/foo.txt', 'r+') as f:
			f.readline()
			f.truncate()  # 没有指定size，则重置到当前位置
			print('Lines after line truncate: ' + str(f.readlines()))
		with open('tmp/foo.txt', 'r+') as f:
			f.truncate(2)  # 指定了可选参数size，则表示截断文件为size 个字符
			print('Lines after str truncate: ' + str(f.readlines()))
			f.seek(0, 0)
			f.write('A: Python is great computer language.\nB: Yes, indeed.\n')  # 将string写入到文件中,然后返回写入的字符数

	def test_write(self):
		with open('tmp/foo.txt', 'r+') as f:
			f.seek(0, 2)  # 在文件末尾写入一行
			f.write('Additional line\n')

	def test_write_lines(self):
		"""
		writelines() 方法用于向文件中写入一序列的字符串。
		这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
		换行需要制定换行符 \n。
		"""
		with open('tmp/foo.txt', 'r+') as f:
			seq = ['write\n', 'lines']
			f.seek(0, 2)
			f.writelines(seq)

	def test_glob(self):
		"""
		glob()函数是一个更强大版本的listdir()函数。它可以让你通过使用模式匹配来搜索文件
		"""
		files = glob.glob("*.py")
		print("Glob pattern: " + str(files))

	@staticmethod
	def multiple_glob(*patterns):
		return itertools.chain.from_iterable(glob.glob(pattern) for pattern in patterns)

	def test_multiple_glob(self):
		it = self.multiple_glob("*.py", "*.txt")
		for file in list(it):
			print("Glob patterns: " + os.path.realpath(file))

	def test_serialize(self):
		print("***** module pickle *****")
		print(dir(pickle))

		var = [1, 'Python', [1.01, 'abc'], ('a', 'b')]
		serialized_var = pickle.dumps(var)
		with open('tmp/serial.txt', 'wb')as f:
			f.write(serialized_var)

	def test_deserialize(self):
		with open("tmp/serial.txt", "rb") as f:
			print(pickle.load(f))


if __name__ == '__main__':
	unittest.main()
