from collections import deque
from typing import Optional, List

from utils.utils import TreeNode, print_tree


class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		stack = deque()
		res = []
		cur = root
		while stack or cur:
			while cur:
				stack.append(cur)
				cur = cur.left

			cur = stack.pop()
			res.append(cur.val)
			cur = cur.right

		return res


if __name__ == "__main__":
	sol = Solution()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(5)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)

	print_tree(root)
	print(sol.inorderTraversal(root))
