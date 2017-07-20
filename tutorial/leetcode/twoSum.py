"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums, target):
	list_ = []
	for i, m in enumerate(nums):
		for j, n in enumerate(nums):
			if m + n == target and i is not j:
				list_.append(i)
				list_.append(j)
				return list_


nums = [3, 3]
target = 6
print(twoSum(nums, target))
