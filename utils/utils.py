from collections import deque
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def print_tree(root: Optional[TreeNode]):
	if not root:
		print("Tree is empty")
		return

	queue = deque([root])
	result = []

	while queue:
		node = queue.popleft()
		if node:
			result.append(str(node.val))
			queue.append(node.left)
			queue.append(node.right)
		else:
			result.append("None")

	# Remove trailing "None" values
	while result and result[-1] == "None":
		result.pop()

	print(" ".join(result))
