"""
Write a function to find the longest common prefix string amongst an array of strings.

"""


def longestCommonPrefix(strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	if len(strs) > 0:
		common = strs[0]
		for str in strs[1:]:
			while not str.startswith(common):
				common = common[:-1]
		return common
	else:
		return ''


print(longestCommonPrefix(['a', 'a']))
