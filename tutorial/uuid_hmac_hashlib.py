import unittest
import uuid
import hmac
import hashlib


class PythonUUIDHmacHashlib(unittest.TestCase):
	def test_uuid(self):
		"""
		即使字符串是唯一的，但它们后边的几个字符看起来很相似。这是因为生成的字符串与电脑的MAC地址是相联系的
		"""
		print("***** module uuid *****")
		print(dir(uuid))
		result = uuid.uuid1()
		print("uuid: " + str(result))

	def test_hmac(self):
		print("***** module hmac *****")
		print(dir(hmac))
		key = bytes('1', 'UTF-8')
		msg = bytes('a', 'UTF-8')
		print("hmac sha256: " + hmac.new(key, msg, hashlib.sha256).hexdigest())

	def test_hashlib(self):
		print("\n***** module hashlib *****")
		print(dir(hashlib))
		m = hashlib.sha1()
		msg = bytes('Java', 'UTF-8')
		m.update(msg)
		print(m.hexdigest())


if __name__ == "__main__":
	unittest.main()
