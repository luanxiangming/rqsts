import unittest


class PythonString(unittest.TestCase):
	""" http://www.runoob.com/python3/python3-tutorial.html """

	def test_string(self):
		self.assertEqual('abC1'.capitalize(), 'Abc1')
		self.assertEqual('abC1'.title(), 'Abc1')
		self.assertEqual('abcD'.swapcase(), 'ABCd')  # 对字符串的大小写字母进行转换
		self.assertEqual('abcd'.center(6, '*'), '*abcd*')  # 返回一个指定的宽度width居中的字符串，fillchar 为填充的字符，默认为空格
		self.assertEqual('abaa'.count('a', 0, 2), 1)  # 统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置
		self.assertTrue('abc'.endswith('c'))

		self.assertEqual('firsts'.find('s'), 3);
		self.assertEqual('first'.find('w'), -1)  # 如果包含子字符串返回开始的索引值，否则返回-1
		self.assertEqual('firsts'.rfind('s'), 5)  # 返回字符串最后一次出现的位置，如果没有匹配项则返回-1
		self.assertEqual('firsts'.index('s'), 3)  # 与find()方法一样，只不过如果str不在string中会报一个异常ValueError
		self.assertEqual('firsts'.rindex('s'), 5)  # 类似于index()，不过是从右边开始

		self.assertTrue('runoob2016'.isalnum());
		self.assertFalse('www runoob.2016'.isalnum())  # 检测字符串是否由字母和数字组成
		self.assertTrue('runoob'.isalpha());
		self.assertFalse('runoob2016'.isalpha())  # 检测字符串是否只由字母组成
		self.assertTrue('1234'.isdigit());
		self.assertFalse('一二三四'.isdigit())  # 检测字符串是否只由数字组成
		self.assertTrue('一二三四'.isnumeric())  # 检测字符串是否只由数字组成。这种方法是只针对unicode对象，包含汉字数字
		self.assertTrue('23444'.isdecimal());
		self.assertFalse('abc123'.isdecimal())  # 检查字符串是否只包含十进制字符,这种方法只存在于unicode对象

		self.assertTrue('runoob..wow!!'.islower());
		self.assertFalse('RUNOOB..wow!!'.islower())  # 检测字符串是否由小写字母组成
		self.assertTrue('   '.isspace())  # 判断所有字符都是空白字符、\t、\n、\r
		self.assertTrue('This Is Title Format.'.istitle());  # 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
		self.assertTrue('ABC...DEF'.isupper())  # 检测字符串中所有的字母是否都为大写
		self.assertEqual('-'.join(('1', '2', '3')), '1-2-3')  # 将序列中的元素以指定的字符连接生成一个新的字符串

		self.assertEqual('abcd'.ljust(10, '*'), 'abcd******')  # 返回一个原字符串左对齐,并使用fillchar填充至长度width的新字符串
		self.assertEqual('abcd'.rjust(10, '*'), '******abcd')  # 返回一个原字符串右对齐,并使用fillchar填充至长度width的新字符串
		self.assertEqual('abcd'.zfill(10), '000000abcd')  # 返回指定长度的字符串，原字符串右对齐，前面填充0
		self.assertEqual('  abc'.lstrip(), 'abc');
		self.assertEqual('888abc'.lstrip('8'), 'abc')  # 截掉字符串左边的空格或指定字符
		self.assertEqual('abc  '.rstrip(), 'abc');
		self.assertEqual('abc888'.rstrip('8'), 'abc')  # 截掉字符串右边的空格或指定字符
		self.assertEqual('**abcd*****'.strip('*'), 'abcd')  # 移除字符串头尾指定的字符（默认为空格）

		# 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
		transtab = str.maketrans('aeiou', '12345')
		self.assertEqual('this is string example....wow'.translate(transtab), 'th3s 3s str3ng 2x1mpl2....w4w')

		self.assertEqual(max('aeiou'), 'u')  # 返回字符串中最大的字母
		self.assertEqual(min('aeiouV'), 'V')  # 返回字符串中最小的字母
		self.assertEqual('This is island'.replace('is', 'was', 2), 'Thwas was island')  # 把将字符串中的str1替换成str2,如果max指定则替换不超过max次
		self.assertEqual('this is string example'.split('t', 1), ['', 'his is string example'])  # 指定分隔符对字符串进行切片,仅分隔num个子字符串
		self.assertEqual('ab c\n\nde fg\rkl\r\n'.splitlines(), ['ab c', '', 'de fg', 'kl'])  # 按照行('\r','\r\n',\n')分隔,返回一个包含各行作为元素的列表
		self.assertEqual('ab c\n\nde fg\rkl\r\n'.splitlines(True), ['ab c\n', '\n', 'de fg\r', 'kl\r\n'])  # 参数keepends为False,不包含换行符;为True,保留换行符
		self.assertTrue('this is string'.startswith('th'));
		self.assertFalse('this is string'.startswith('th', 2))  # 参数beg和end指定值，则在指定范围内检查


if __name__ == "__main__":
	unittest.main()
