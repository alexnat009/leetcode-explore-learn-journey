from typing import Optional, List

from utils.utils import TreeNode


class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []

		result = []
		stack = [root]
		while stack:
			current = stack.pop()
			result.append(current.val)
			if current.right:
				stack.append(current.right)
			if current.left:
				stack.append(current.left)
		return result
