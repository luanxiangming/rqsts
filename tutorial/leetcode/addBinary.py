"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def addBinary(a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	if a == '0' and b == '0':
		return '0'
	return bin(int('0b' + a, 2) + int('0b' + b, 2)).lstrip('0b')


print(addBinary('11', '1'))
print(addBinary('0', '0'))
print(addBinary('0', '11'))
