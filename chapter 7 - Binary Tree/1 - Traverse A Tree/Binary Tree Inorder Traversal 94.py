from typing import Optional, List

from utils.utils import TreeNode


class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		result = []
		stack = []
		current = root
		while stack or current:
			if current:
				stack.append(current)
				current = current.left
			else:
				current = stack.pop()
				result.append(current.val)
				current = current.right
		return result
