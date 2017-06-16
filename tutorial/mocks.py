import requests
from unittest.mock import Mock, MagicMock, patch
import unittest


class TestClient(unittest.TestCase):
	def send_request(self, url):
		return requests.get(url).status_code

	def visit_ustack(self):
		return self.send_request('http://www.ustack.com')

	def test_success_request(self):
		success_send = Mock(return_value='200')
		self.send_request = success_send
		self.assertEqual(self.visit_ustack(), '200')

	def test_fail_request(self):
		fail_send = Mock(return_value='404')
		self.send_request = fail_send
		self.assertEqual(self.visit_ustack(), '404')

	# Mock对象的call_args表示该mock对象被调用的tuple，tuple的每个成员都是一个mock.call对象。
	# mock.call这个对象代表了一次对mock对象的调用，其内容是一个tuple，含有两个元素，
	# 第一个元素是调用mock对象时的位置参数（*args），第二个元素是调用mock对象时的关键字参数（**kwargs）
	def test_call_sent_with_correct_arguments(self):
		self.send_request = Mock()
		self.visit_ustack()
		self.assertEqual(self.send_request.called, True)
		call_args = self.send_request.call_args
		self.assertIsInstance(call_args[0][0], str)
		print(call_args[0][0])

	# 在了解了mock对象之后，我们来看两个方便测试的函数：patch和patch.object。
	# 这两个函数都会返回一个mock内部的类实例，这个类是class _patch。返回的这个类实例既可以作为函数的装饰器，也可以作为类的装饰器，也可以作为上下文管理器。
	# 使用patch或者patch.object的目的是为了控制mock的范围，意思就是在一个函数范围内，或者一个类的范围内，或者with语句的范围内mock掉一个对象
	def test_success_uses_patch(self):
		status_code = 200
		success_send = Mock(return_value=status_code)
		with patch('mocks.TestClient.send_request', success_send):
			self.assertEqual(self.visit_ustack(), status_code)

	# patch.object和patch的效果是一样的，只不过用法有点不同
	def test_fail_uses_patch(self):
		status_code = 404
		fail_send = Mock(return_value=status_code)
		with patch.object(self, 'send_request', fail_send):
			self.assertEqual(self.visit_ustack(), status_code)


class ProductionClass(unittest.TestCase):
	# 26.5.1.1. Mock Patching Methods
	def method(self):
		self.something(1, 2, 3)

	def something(self, a, b, c):
		pass

	def test_assert_called_once_with(self):
		real = ProductionClass()
		real.something = MagicMock()
		real.method()
		real.something.assert_called_once_with(1, 2, 3)

	# 26.5.1.2. Mock for Method Calls on an Object
	def closer(self, something):
		something.close()

	def test_assert_called_with(self):
		real = ProductionClass()
		something = Mock()
		real.closer(something)
		something.close.assert_called_with()

	# 26.5.1.3. Mocking Classes
	class Foo:
		def method(self):
			pass

	def some_function(self):
		instance = self.Foo()
		return instance.method()

	def test_patch(self):
		with patch('mocks.ProductionClass.Foo') as mock:
			instance = mock.return_value
			instance.method.return_value = 'the result'
			result = self.some_function()
			assert result == 'the result'

	# 26.5.1.6. Setting Return Values and Attributes
	def test_object_return_value(self):
		# Setting the return values on a mock object
		mock = Mock()
		mock.return_value = 3
		print(mock())
		# same for methods on the mock
		mock.method.return_value = 4
		print(mock.method())
		# The return value can also be set in the constructor:
		mock = Mock(return_value=5)
		print(mock())
		# Attribute setting on mock
		mock = Mock()
		mock.x = 6
		print(mock.x)

	# 26.5.1.7. Raising exceptions with mocks
	@unittest.skip
	def test_exceptions_with_mock(self):
		mock = Mock(side_effect=Exception('Boom!'))
		print(mock())

	# 26.5.1.8. Side effect functions and iterables
	def test_side_effect_iterables(self):
		mock = MagicMock(side_effect=[3, 4, 5])
		self.assertEqual(mock(), 3)
		self.assertEqual(mock(), 4)
		self.assertEqual(mock(), 5)

	def side_effect(self, *args):
		vals = {(1, 2): 1, (2, 3): 2}
		return vals[args]

	def test_side_effect_functions(self):
		mock = MagicMock(side_effect=self.side_effect)
		print(mock(1, 2))
		print(mock(2, 3))


if __name__ == '__main__':
	unittest.main()
