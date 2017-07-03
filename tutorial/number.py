import unittest, random, math


class PythonNumbers(unittest.TestCase):
	# 数学函数
	def test_math_functions(self):
		self.assertEqual(abs(-10), 10)
		self.assertEqual(math.ceil(4.1), 5)  # 数字的上入整数
		self.assertEqual(math.floor(3.9), 3)  # 数字的下舍整数
		self.assertEqual(math.exp(1), 2.718281828459045)  # 返回e的x次幂
		self.assertEqual(math.fabs(-10), 10.0)  # 返回数字的绝对值
		self.assertEqual(math.log(100, 10), 2.0)
		self.assertEqual(math.log10(100), 2.0)
		self.assertEqual(max(1, 2, 2.2), 2.2)
		self.assertEqual(min(-1, -2, -3.2), -3.2)
		self.assertEqual(math.modf(-3.0), (-0.0, -3.0))  # 返回整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
		self.assertEqual(math.pow(100, -2), 100 ** -2)  # x**y 运算后的值
		self.assertEqual(round(56.659, 1), 56.7)  # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
		self.assertEqual(math.sqrt(4), 2.0)  # 返回数字x的平方根

	# 随机数函数
	def test_random(self):
		print('\n')
		print('Random number between 1~6: %s' % random.choice(range(1, 7)))
		print('Random number between 1~6: %s' % random.randint(1, 6))
		print('Random number between 0~6: %s' % random.randrange(7))
		print('Random odd number between 1~9: %s' % random.randrange(1, 10, 2))  # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
		print('Random number between 0~1: %s' % random.random())  # 返回随机生成的一个实数，它在[0,1)范围内
		list_ = [1, 2, 3];
		random.shuffle(list_)  # 将序列的所有元素随机排序
		print('Random shuffled list: %s' % list_)
		print('Random number between given range: %s' % random.uniform(math.e, math.pi))  # 随机生成下一个实数，它在[x,y]范围内


if __name__ == '__main__':
	unittest.main()
