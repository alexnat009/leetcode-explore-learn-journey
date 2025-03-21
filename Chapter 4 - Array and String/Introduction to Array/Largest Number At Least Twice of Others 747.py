from typing import List


class Solution:
	def dominantIndex(self, nums: List[int]) -> int:
		tmp = sorted(nums)
		cond = tmp[-1] >= tmp[-2] * 2
		return nums.index(tmp[-1]) if cond else -1


if __name__ == "__main__":
	sol = Solution()

	nums = [3, 6, 1, 0]
	print(sol.dominantIndex(nums))
