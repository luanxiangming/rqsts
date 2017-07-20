"""
Determine whether an integer is a palindrome. Do this without extra space.

"""


def isPalindrome(x):
	"""
	:type x: int
	:rtype: bool
	"""
	if x >= 0:
		y = str(x)
		l = len(y)
		for i in range(l // 2):
			if y[i] == y[l - i - 1]:
				continue
			else:
				return False
		else:
			return True
	else:
		return False


print(isPalindrome(0))
