"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	x_max = 2 ** 31 - 1
	x_min = -x_max

	if 0 <= x < x_max:
		x = str(x)
		x = x[::-1]
		y = int(x)
	elif x_min < x < 0:
		y = -reverse(abs(x))
	else:
		y = 0

	if x_min < y < x_max:
		return y
	else:
		return 0


print(reverse(1233))
print(reverse(0))
print(reverse(-1283))
print(reverse(1100))
print(reverse(1534236469))
print(reverse(1563847412))
print(reverse(-2147483412))
