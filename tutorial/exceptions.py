import sys
import unittest


class BaseError(Exception):
	""" 用户自定义异常, 异常应该继承自 Exception 类，或者直接继承，或者间接继承 """

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


class InputError(BaseError):
	"""当创建一个模块有可能抛出多种不同的异常时，
	一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类
	"""

	def __init__(self, expression, message):
		self.expression = expression
		self.message = message


class PythonException(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_exception(self):
		try:
			with open('tmp/foo.txt', 'r+') as f:
				line = f.readline()
				count = int(line)

				''' raise手动抛出一个指定的异常,参数指定了要被抛出的异常。它必须是Exception的子类 
				raise ValueError('Exception: cannot covert to integer')
				'''
				print('Line length: ' + len(line))
		except ValueError:
			print('Exception: ValueError')
		# raise #如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
		except TypeError:
			print('Exception: TypeError')
		except:  # 忽略异常的名称，它将被当作通配符使用raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）
			print('Unexpected Error: ' + str(sys.exc_info()))

		else:  # 放在所有的except子句之后, 将在try子句没有发生任何异常的时候执行
			print('No Exceptions.')

		finally:  # 不管try子句里面有没有发生异常，finally子句都会执行
			print('End of execution.')

	def test_custom_exception(self):
		try:
			raise InputError('Enter non-null message', '404')
		except InputError as e:
			print('Custom Exception:\n\t Expression: {0}\n\t Message: {1}'.format(e.expression, e.message))


if __name__ == '__main__':
	unittest.main()
