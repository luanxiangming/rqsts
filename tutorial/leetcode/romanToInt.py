"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
from functools import reduce


def romanToInt(s):
	"""
	:type s: str
	:rtype: int
	"""
	dict_ = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	# return reduce(lambda foo, y: foo + dict_[y] if (dict_[y] < foo) else dict_[y] - foo, s, 0)
	total = 0
	prev = 0
	for i in reversed(s):
		if dict_.get(i) < prev:
			total = total - dict_.get(i)
		else:
			total += dict_.get(i)
		prev = dict_.get(i)
	return total


print(romanToInt('X'))
print(romanToInt('MCMXCVI'))

