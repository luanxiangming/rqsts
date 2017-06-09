import unittest, os, shutil, glob, sys, re, math, random, zlib, doctest
from urllib import request
from datetime import date
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
		print(dir(os)) #返回模块函数列表
		print(os.getcwd())
		os.system('date') #执行系统命令
		# help(os) #返回模块用户手册
		
	
	''' 针对日常的文件和目录管理任务, shutil模块提供了一个易于使用的高级接口 '''
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
		print(random.sample(range(100), 10)) # sampling without replacement
		print(random.randrange(10))

	def test_urllib_request(self):
		print('module request: ')
		print(dir(request))
		for line in request.urlopen('http://www.jd.com'):
			line = line.decode('utf-8')
			if '京东618' in line:
				print(line)
	
	def test_date(self):
		'''python中时间日期格式化符号：
		%y 两位数的年份表示（00-99）
		%Y 四位数的年份表示（000-9999）
		%m 月份（01-12）
		%d 月内中的一天（0-31）
		%H 24小时制小时数（0-23）
		%I 12小时制小时数（01-12）
		%M 分钟数（00=59）
		%S 秒（00-59）
		%a 本地简化星期名称
		%A 本地完整星期名称
		%b 本地简化的月份名称
		%B 本地完整的月份名称
		%c 本地相应的日期表示和时间表示
		%j 年内的一天（001-366）
		%p 本地A.M.或P.M.的等价符
		%U 一年中的星期数（00-53）星期天为星期的开始
		%w 星期（0-6），星期天为星期的开始
		%W 一年中的星期数（00-53）星期一为星期的开始
		%x 本地相应的日期表示
		%X 本地相应的时间表示
		%Z 当前时区的名称
		%% %号本身
		'''
		print('module date: ')
		print(dir(date))
		print(date.today())
		print(date.today().strftime('%d-%m-%y. %d %b %Y is a %a on the %dth day of %B'))

		birthday = date(1983, 7, 14)
		print(date.today() - birthday) # dates support calendar arithmetic

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
		doctest.testmod(verbose=True) #实例在test.py

		

if __name__ == '__main__':
	unittest.main()