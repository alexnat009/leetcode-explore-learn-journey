# Definition for a binary tree node.
from typing import Optional

from utils.utils import TreeNode, print_tree


class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if not root:
			return None

		self.invertTree(root.left)
		self.invertTree(root.right)
		root.left, root.right = root.right, root.left
		return root


if __name__ == "__main__":
	root = TreeNode(4,
					TreeNode(2, TreeNode(1), TreeNode(3)),
					TreeNode(7, TreeNode(6), TreeNode(9)))

	print_tree(root)

	sol = Solution()
	inverted_root = sol.invertTree(root)

	print("Inverted Tree:")
	print_tree(inverted_root)
