from typing import List


class Solution:
	def heightChecker(self, heights: List[int]) -> int:
		tmp = sorted(heights)
		k = 0
		for i in range(len(tmp)):
			if tmp[i] != heights[i]:
				k += 1
		return k


if __name__ == "__main__":
	sol = Solution()
	heights = [1, 1, 4, 2, 1, 3]
	print(sol.heightChecker(heights))
