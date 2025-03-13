from typing import Optional

from utils.utils import TreeNode


# Definition for a binary tree node.

class Solution:
	def checkTree(self, root: Optional[TreeNode]) -> bool:
		return root.val == root.left.val + root.right.val


# Test Case
if __name__ == "__main__":
	# Creating a sample tree
	root = TreeNode(10, TreeNode(4), TreeNode(6))

	sol = Solution()
	print(sol.checkTree(root))
