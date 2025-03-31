from collections import deque
from typing import List


class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		n = len(temperatures)
		res = [0] * n
		stack = []
		for idx, temperature in enumerate(temperatures):
			while stack and temperatures[stack[-1]] < temperature:
				stack_idx = stack.pop()
				res[stack_idx] = idx - stack_idx
			stack.append(idx)
		return res


if __name__ == "__main__":
	sol = Solution()
	temperatures = [8, 10, 7, 6, 9, 11]
	print(sol.dailyTemperatures(temperatures))
