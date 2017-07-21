"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from functools import reduce


def letterCombinations(digits):
	"""
	:type digits: str
	:rtype: List[str]
	"""
	if digits == '':
		return []
	dict_ = {
		"1": '',
		"2": 'abc',
		"3": 'def',
		"4": 'ghi',
		"5": 'jkl',
		"6": 'mno',
		"7": 'pqrs',
		"8": 'tuv',
		"9": 'wxyz'
	}

	return reduce(lambda foo, digit: [x + y for x in foo for y in dict_[digit]], digits, [''])


print(letterCombinations('454'))
