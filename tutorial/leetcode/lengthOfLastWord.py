"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


def lengthOfLastWord(s):
	"""
	:type s: str
	:rtype: int
	"""
	if s.strip() == '':
		return 0
	list_ = s.strip().split(" ")
	for i in range(list_.count('')):
		list_.remove('')
	return len(list_[-1])


print(lengthOfLastWord("Hello World1 ede"))
print(lengthOfLastWord("a "))
print(lengthOfLastWord("a"))
print(lengthOfLastWord(""))
print(lengthOfLastWord("b aa   "))
print(lengthOfLastWord(" "))
print(lengthOfLastWord("        "))
