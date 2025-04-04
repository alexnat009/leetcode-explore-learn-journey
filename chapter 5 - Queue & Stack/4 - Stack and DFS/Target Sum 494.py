from typing import List, Dict, Tuple


class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		memo: Dict[Tuple[int, int], int] = {}

		def dfs(index: int, current_sum: int) -> int:
			if index == len(nums):
				return 1 if current_sum == target else 0

			if (index, current_sum) in memo:
				return memo[(index, current_sum)]

			add = dfs(index + 1, current_sum + nums[index])
			subtract = dfs(index + 1, current_sum - nums[index])

			memo[(index, current_sum)] = add + subtract

			return memo[(index, current_sum)]

		return dfs(0, 0)


if __name__ == "__main__":
	sol = Solution()
	nums = [1, 1, 1, 1, 1]
	target = 3

	print(sol.findTargetSumWays(nums, target))
