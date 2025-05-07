from typing import Optional, List

from utils.utils import TreeNode


class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		return root.val + self.preorderTraversal(root.left) + root.val + self.preorderTraversal(root.right)

