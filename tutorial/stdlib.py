import unittest, os, shutil, glob, sys, re, math, random, zlib, doctest
from urllib import request
from timeit import Timer


class PythonStdLib(unittest.TestCase):
	def setUp(self):
		self.origin = os.getcwd()
		print('\n')

	def tearDown(self):
		os.chdir(self.origin)

	''' 操作系统接口 '''

	def test_os(self):
		print('module os: ')
		print(dir(os))  # 返回模块函数列表
		print(os.getcwd())
		os.system('date')  # 执行系统命令
	# help(os) #返回模块用户手册

	'''针对日常的文件和目录管理任务,shutil模块提供了一个易于使用的高级接口'''

	def test_shutil(self):
		print('module shutil: ')
		print(dir(shutil))
		shutil.copyfile('tmp/data.pkl', 'tmp/data_backup.pkl')
		self.assertTrue(os.path.exists('tmp/data_backup.pkl'))
		# self.assertTrue(os.access('tmp/data_backup.pkl', os.F_OK))

		shutil.move('tmp/data_backup.pkl', 'data_backup.pkl')
		self.assertTrue(os.path.exists('data_backup.pkl'))

		os.remove('data_backup.pkl')
		self.assertFalse(os.path.exists('data_backup.pkl'))
		self.assertFalse(os.path.exists('tmp/data_backup.pkl'))

	''' 文件通配符
	glob模块提供了一个函数用于从目录通配符搜索中生成文件列表 '''

	def test_glob(self):
		print(glob.glob('*.py'))

	''' 命令行参数 '''

	def test_argv(self):
		print(sys.argv)

	''' 错误输出重定向和程序终止
	sys 有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息 '''

	def test_stderr(self):
		print('module sys: ')
		print(dir(sys))
		sys.stderr.write('Warning! Log file not found')
		sys.exit

	''' 字符串正则匹配
	re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案
	'''

	def test_re(self):
		print('module re: ')
		print(dir(re))
		match = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
		print(match)

		match = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
		print(match)

	def test_math(self):
		print('module math: ')
		print(dir(math))

	def test_random(self):
		print('module random: ')
		print(dir(random))
		print(random.choice(['apple', 'pear', 'banana']))
		print(random.sample(range(100), 10))  # sampling without replacement
		print(random.randrange(10))

	def test_urllib_request(self):
		print('module request: ')
		print(dir(request))
		for line in request.urlopen('http://www.jd.com'):
			line = line.decode('utf-8')
			if '京东618' in line:
				print(line)

	'''数据压缩
	模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile
	'''

	def test_zlib(self):
		print('module zlib: ')
		print(dir(zlib))
		raw = b'witch which has which witches wrist watch'
		self.assertEqual(len(raw), 41)

		compress = zlib.compress(raw)
		self.assertEqual(len(compress), 37)

		decompress = zlib.decompress(compress)
		self.assertEqual(decompress, raw)
		self.assertEqual(len(decompress), 41)

	# 相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具
	def test_timer(self):
		print('module timer: ')
		print(dir(Timer))
		old = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
		new = Timer('a,b=b,a', 'a=1;b=2').timeit()
		self.assertLess(new, old)

	def test_doctest(self):
		print('module doctest: ')
		print(dir(doctest))
		doctest.testmod(verbose=True)  # 实例在test.py


if __name__ == '__main__':
	unittest.main()
