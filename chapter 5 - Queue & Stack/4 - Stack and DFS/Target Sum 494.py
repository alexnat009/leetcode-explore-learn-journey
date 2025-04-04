from typing import List


class Solution:
	def __init__(self):
		self.total_ways = 0

	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		self.calculate_ways(nums, 0, 0, target)
		return self.total_ways

	def calculate_ways(self, nums: List[int], current_index: int, current_sum: int, target: int):
		if current_index == len(nums):
			if current_sum == target:
				self.total_ways += 1
		else:
			self.calculate_ways(nums, current_index + 1, current_sum + nums[current_index], target)
			self.calculate_ways(nums, current_index + 1, current_sum - nums[current_index], target)


if __name__ == "__main__":
	sol = Solution()
	nums = [1, 1, 1, 1, 1]
	target = 3

	print(sol.findTargetSumWays(nums, target))
