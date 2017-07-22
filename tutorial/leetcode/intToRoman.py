"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


def intToRoman(num):
	"""
	:type num: int
	:rtype: str
	"""
	dict_ = {
		1: 'I',
		5: 'V',
		10: 'X',
		50: 'L',
		100: 'C',
		500: 'D',
		1000: 'M'
	}
	result = ''
	remain = num
	while remain != 0:
		for i in sorted(dict_, reverse=True):
			if i <= remain:
				result += dict_.get(i)
				remain -= i
				break
	return result


print(intToRoman(1))
print(intToRoman(4))
print(intToRoman(99))

print(intToRoman(2))
print(intToRoman(11))
print(intToRoman(9))
