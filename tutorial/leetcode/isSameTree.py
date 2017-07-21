"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""


def isSameTree(p, q):
	"""
	:type p: TreeNode
	:type q: TreeNode
	:rtype: bool
	"""
	if p and q:
		return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
	return p is q


print(isSameTree('', ''))
