from typing import List
from collections import deque


class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:

		def changes(code):
			for i in range(len(code)):
				for delta in [-1, 1]:
					new_digit = (int(code[i]) + delta) % 10

					yield code[:i] + str(new_digit) + code[i + 1:]

		root = "0000"
		if root == target:
			return 0
		deadends = set(deadends)
		if root in deadends:
			return -1

		front = {root}
		back = {target}
		visited = {root, target}
		step = 0
		while front and back:
			step += 1
			if len(front) > len(back):
				front, back = back, front
			next_level = set()
			for lock in front:
				for variants in changes(lock):
					if variants in back:
						return step
					if variants not in visited and variants not in deadends:
						visited.add(variants)
						next_level.add(variants)
			front = next_level
		return -1


if __name__ == "__main__":
	sol = Solution()

	deadends = ["0201", "0101", "0102", "1212", "2002"]
	target = "0202"
	print(sol.openLock(deadends, target))
