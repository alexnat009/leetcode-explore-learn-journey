from collections import deque
from typing import Optional, List

from utils.utils import TreeNode


class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []

		queue = deque([root])
		result = []
		while queue:
			n = len(queue)
			level = []
			for _ in range(n):
				current = queue.popleft()
				level.append(current.val)
				if current.left:
					queue.append(current.left)
				if current.right:
					queue.append(current.right)
			result.append(level)
		return result


def build_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
	if not nodes:
		return None

	root = TreeNode(nodes[0])
	queue = deque([root])
	i = 1

	while queue and i < len(nodes):
		current = queue.popleft()
		if nodes[i] is not None:
			current.left = TreeNode(nodes[i])
			queue.append(current.left)
		i += 1

		if i < len(nodes) and nodes[i] is not None:
			current.right = TreeNode(nodes[i])
			queue.append(current.right)
		i += 1

	return root


# 4. Main function to test
if __name__ == "__main__":
	test_cases = [
		[3, 9, 20, None, None, 15, 7],
		[1],
		[],
		[1, 2, 3, 4, None, None, 5]
	]
	sol = Solution()
	for i, test in enumerate(test_cases):
		root = build_tree(test)
		print(f"Test Case {i + 1}: Input = {test}")
		print("Output =", sol.levelOrder(root))
		print("---")
