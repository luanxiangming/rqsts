"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
from functools import reduce


def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	return reduce(lambda x, y: x ^ y, nums)


print(singleNumber([1, 1, 2, 3, 2]))
print(singleNumber([1]))
