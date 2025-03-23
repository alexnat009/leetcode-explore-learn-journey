from typing import List


class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		n = len(nums)
		left = 0
		currentSum = 0
		minSubArray = float("inf")
		for right in range(n):
			currentSum += nums[right]
			while currentSum >= target:
				minSubArray = min(minSubArray, right - left + 1)
				currentSum -= nums[left]
				left += 1
		return minSubArray if minSubArray != float('inf') else 0


if __name__ == "__main__":
	sol = Solution()
	target = 6
	nums = [10, 2, 3]
	# target = 7
	# nums = [2, 3, 1, 2, 4, 3]
	print(sol.minSubArrayLen(target, nums))
