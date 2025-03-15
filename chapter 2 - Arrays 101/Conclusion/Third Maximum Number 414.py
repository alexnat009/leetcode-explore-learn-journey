from typing import List


class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		tmp = set(nums)
		if len(tmp) < 3:
			return max(tmp)
		else:
			tmp.remove(max(tmp))
			tmp.remove(max(tmp))
			return max(tmp)


if __name__ == "__main__":
	sol = Solution()
	heights = [1, 1, 1, 1, 14]
	print(sol.thirdMax(heights))
