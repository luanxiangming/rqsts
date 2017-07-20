import sys

"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


def divide(dividend, divisor):
	"""
	:type dividend: int
	:type divisor: int
	:rtype: int
	"""

	result = dividend / divisor
	if result > sys.maxsize:
		result = sys.maxsize
	elif result < sys.maxsize * (-1):
		result = sys.maxsize * (-1)
	return result

print(sys.maxsize)
print(divide(-2147483648, -1))
