import re, unittest

class PythonRe(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		print('Module Re: ')
		print(dir(re))

	''' re.match 尝试从字符串的起始位置匹配一个模式 '''
	def test_match(self):
		self.assertEqual(re.match('www', 'www.google.com').span(), (0, 3)) # 在起始位置匹配
		self.assertIsNone(re.match('com', 'www.google.com')) # 不在起始位置匹配

		line = 'Cats are smarter than dogs'
		m = re.match(r'(.*) are (.*?) .*', line)
		self.assertEqual(m.group(0), line)
		self.assertEqual(m.group(1), 'Cats')
		self.assertEqual(m.group(2), 'smarter')
		self.assertEqual(m.groups(), ('Cats', 'smarter'))

	''' re.search 扫描整个字符串并返回第一个成功的匹配 '''
	def test_search(self):
		self.assertEqual(re.search('www', 'www.google.com').span(), (0, 3)) # 在起始位置匹配
		self.assertEqual(re.search('com', 'www.google.com').span(), (11, 14)) # 不在起始位置匹配

		line = 'Cats are smarter than dogs'
		m = re.search(r'(.*) are (.*?) .*', line)
		self.assertEqual(m.group(0), line)
		self.assertEqual(m.group(1), 'Cats')
		self.assertEqual(m.group(2), 'smarter')

	'''检索和替换
	re.sub用于替换字符串中的匹配项
	re.sub(pattern, repl, string, count=0)'''
	def add_it(self, matched):
		value = int(matched.group('value'))
		return str(value + 1)
	def test_sub(self):
		phone = "2004-959-559 #这是一个电话号码"
		remove_comment = re.sub('#.*', '', phone) # 删除注释
		self.assertEqual(remove_comment, '2004-959-559 ')

		remove_space = re.sub('\s', '', remove_comment)
		self.assertEqual(remove_space, '2004-959-559')

		remove_non_decimal_digit = re.sub('\D', ' ', remove_space) # 移除非数字的内容
		self.assertEqual(remove_non_decimal_digit, '2004 959 559')

		add_it = re.sub('(?P<value>\d+)', self.add_it, remove_non_decimal_digit) # 当 repl 参数是一个函数
		self.assertEqual(add_it, '2005 960 560')


	def test_flags(self):
		'''修饰符 - 可选标志
		正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志
		re.I	使匹配对大小写不敏感
		re.L	做本地化识别（locale-aware）匹配
		re.M	多行匹配，影响 ^ 和 $
		re.S	使 . 匹配包括换行在内的所有字符
		re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
		re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
		'''
		pass

	def test_model(self):
		''' 正则表达式模式
		^	匹配字符串的开头
		$	匹配字符串的末尾。
		.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
		[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
		[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
		re*	匹配0个或多个的表达式。
		re+	匹配1个或多个的表达式。
		re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
		re{ n}	
		re{ n,}	精确匹配n个前面表达式。
		re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
		a| b	匹配a或b
		(re)	G匹配括号内的表达式，也表示一个组
		(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
		(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
		(?: re)	类似 (...), 但是不表示一个组
		(?imx: re)	在括号中使用i, m, 或 x 可选标志
		(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
		(?#...)	注释.
		(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
		(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
		(?> re)	匹配的独立模式，省去回溯。
		\w	匹配字母数字
		\W	匹配非字母数字
		\s	匹配任意空白字符，等价于 [\t\n\r\f].
		\S	匹配任意非空字符
		\d	匹配任意数字，等价于 [0-9].
		\D	匹配任意非数字
		\A	匹配字符串开始
		\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
		\z	匹配字符串结束
		\G	匹配最后匹配完成的位置。
		\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
		\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
		\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
		\1...\9	匹配第n个分组的内容。
		\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。
		'''
		pass



if __name__ == '__main__':
	unittest.main()