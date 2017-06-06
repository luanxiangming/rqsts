import unittest

class PythonLoops(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_while(self):
		sum = 0
		num = 1
		while num <= 100:
			sum += num
			num += 1
		self.assertEqual(sum, 5050)
			
	def test_while_else(self):
		count = 0
		while count < 5:
			self.assertLess(count, 5)
			count += 1
		else:
			self.assertEqual(count, 5)

	def test_for(self):
		languages = ["C", "C++", "Perl", "Python"]
		for lang in languages:
			print(lang)

	def test_for_break(self):
		sites = ["Baidu", "Google","Runoob","Taobao"]
		for site in sites:
			if site == 'Runoob':
				print('Run into Runoob, exit...')
				break
			print(site)

	# 循环语句可以有else子句，它在穷尽列表(以for循环)或条件变为false(以while循环)导致循环终止时被执行,但循环被break终止时不执行
	def test_for_else(self):
		sites = ["Baidu", "Google","Runoob","Taobao"]
		for site in sites:
			if site == 'Runoob':
				break
			print(site)
		else:
			print('loop ends.')

	def test_range(self):
		print('\n')
		for x in range(5, 9):
			print(x, end=',')
		print('\n')
		for y in range(1,10,2):
			print(y, end=',')
		print('\n')
		for z in range(10,1,-2):
			print(z, end=',')

	def test_index(self):
		a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
		for i in range(len(a)):
			print(i, a[i])

	def test_index_enumerate(self):
		a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
		for index,value in enumerate(a):
			print(index, value)

	# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
	def test_continue(self):
		for letter in 'Python':
			if letter == 't':
				continue
			print(letter, end=' ')


if __name__ == '__main__':
	unittest.main()