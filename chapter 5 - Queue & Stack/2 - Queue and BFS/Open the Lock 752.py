from typing import List
from collections import deque


class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:

		def changes(code):
			variations = []
			for i in range(len(code)):
				for delta in [-1, 1]:
					new_digit = (int(code[i]) + delta) % 10

					variations.append(code[:i] + str(new_digit) + code[i + 1:])
			return variations

		def count_steps(start):
			queue = deque([start])
			visited = {start}
			step = 1
			while queue:
				size = len(queue)
				for _ in range(size):
					current = queue.popleft()
					for variant in changes(current):
						if variant == target:
							return step
						if variant not in deadends and variant not in visited:
							queue.append(variant)
							visited.add(variant)
				step += 1
			return -1

		root = "0000"
		if root == target:
			return 0
		return count_steps(root) if root not in deadends else -1


if __name__ == "__main__":
	sol = Solution()

	deadends = ["0201", "0101", "0102", "1212", "2002"]
	target = "0202"
	print(sol.openLock(deadends, target))
