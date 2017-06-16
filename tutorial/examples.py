import cmath
import unittest


class PythonExamples(unittest.TestCase):
	""" 计算实数和复数平方根
	导入复数数学模块 """

	def test_cmath(self):
		print('module cmath: ')
		print(dir(cmath))
		self.assertEqual(16 ** 0.5, 4.0)
		self.assertEqual(cmath.sqrt(16), (4 + 0j))

	def test_swap(self):
		x, y = 1, 2
		print(x, y)

		tmp = x;
		x = y;
		y = tmp
		print(x, y)

		x, y = y, x
		print(x, y)

	''' 判断闰年 '''

	def test_leap_year(self):
		years = [200, 400, 60, 70, 2100, 2000]
		leap = []
		for year in years:
			if year % 4 == 0:
				if year % 100 == 0:
					if year % 400 == 0:  # 整百年能被400整除的是闰年
						leap.append(year)
				else:
					leap.append(year)  # 非整百年能被4整除的为闰年
		print('Leap years: ' + str(leap))

	'''一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
	换句话说就是该数除了1和它本身以外不再有其他的因数'''

	def test_prime_number(self):
		numbers = range(30, 50)
		primes = []
		for num in numbers:
			if num > 1:
				for i in range(2, num):
					if num % i == 0:
						print(str(num) + ' is NOT prime number!')
						break
				else:
					primes.append(num)
		print('Primes: ' + str(primes))

	'''整数的阶乘是所有小于及等于该数的正整数的积，0的阶乘为1
	即：n!=1×2×3×...×n'''

	def test_factorial(self):
		numbers = range(1, 6)
		factorials = []
		for num in numbers:
			if num >= 1:
				factorial = 1
				for i in range(1, num + 1):
					factorial *= i
				factorials.append(factorial)
		print('Factorials: ' + str(factorials))

	''' 九九乘法表 '''

	def test_multiply_table(self):
		num = range(1, 10)
		for i in num:
			for j in range(1, i + 1):
				print('{}x{}={}'.format(i, j, i * j), end=' ')
			print('\n')

	''' 斐波那契数列 '''

	def test_fibonacci(self):
		count = 20
		list_ = [0, 1]
		for i in range(count):
			num = list_[-2] + list_[-1]
			list_.append(num)
		print('Fibonacci: ' + str(list_))

	''' 阿姆斯特朗数 
	如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
	1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407'''

	def test_armstrongnumber(self):
		numbers = range(1000)
		armstrongnumber = []
		for num in numbers:
			str_num = str(num)
			digit = len(str_num)
			result = 0
			for i in str_num:
				result += int(i) ** digit
			if result == int(str_num):
				armstrongnumber.append(str_num)
		print('Armstrongnumber: ' + str(armstrongnumber))

	''' 十进制转二进制、八进制、十六进制 '''

	def test_transcode(self):
		numbers = [10, 5]
		for num in numbers:
			print('{}转换为10进制为: {}'.format(num, num))
			print('{}转换为8进制为: {}'.format(num, oct(num)))
			print('{}转换为2进制为: {}'.format(num, bin(num)))
			print('{}转换为16进制为: {}'.format(num, hex(num)))

	def test_ascii(self):
		input = ['a', '6', 77]
		for i in input:
			if type(i) == str:
				print('字符{}的ASCII码是: {}'.format(i, ord(i)))
			elif type(i) == int:
				print('数字{}对应的字符是: {}'.format(i, chr(i)))

	''' 最大公约数算法 '''

	def test_greatest_common_divisor(self):
		numbers = [54, 24, 84]
		divisors = []
		commons = []
		for num in numbers:
			for i in range(1, min(numbers) + 1):
				if num % i == 0:
					divisors.append(i)
		print('Divisors: ' + str(divisors))
		for i in divisors:
			if divisors.count(i) == len(numbers):
				commons.append(i)
		print('Common Divisors: ' + str(set(commons)))
		print('Greatest Common Divisor: ' + str(max(commons)))

	''' 最小公倍数算法 '''

	def test_minimum_common_multiply(self):
		x, y = 54, 24
		c = 1
		while True:
			if c % x == 0 and c % y == 0:
				lcm = c
				break
			c += 1
		print('Minimum multiply: ' + str(lcm))

	''' 使用join链接list成为字符串
	使用split分割字符串成为列表, 皆为字符串方法 '''

	def test_join_split_list(self):
		params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
		list_ = ['{}={}'.format(k, v) for k, v in params.items()]  # dictionary中的解析
		joined = ';'.join(list_)
		print('List joined to String: ' + joined)

		restored = joined.split(';')
		print('String splitted to List: ' + str(restored))


if __name__ == '__main__':
	unittest.main()
