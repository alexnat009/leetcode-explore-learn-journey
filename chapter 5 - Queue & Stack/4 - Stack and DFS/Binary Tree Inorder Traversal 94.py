from collections import deque
from typing import Optional, List

from utils.utils import TreeNode, print_tree


class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


if __name__ == "__main__":
	sol = Solution()
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)

	print_tree(root)
	print(sol.inorderTraversal(root))