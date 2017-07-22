"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""


def combinationSum(candidates, target):
	"""
    :type candidates: List[int]
	:type target: int
	:rtype: List[List[int]]
	"""

	result = []
	candidates = sorted(candidates)

	def dfs(remain, stack):
		if remain == 0:
			result.append(stack)
			return

		for item in candidates:
			if item > remain:
				break
			if stack and item < stack[-1]:
				continue
			else:
				dfs(remain - item, stack + [item])

	dfs(target, [])
	return result


print(combinationSum([2, 3, 6, 7], 6))
