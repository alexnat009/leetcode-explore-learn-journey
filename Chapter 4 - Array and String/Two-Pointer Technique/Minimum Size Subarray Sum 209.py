from typing import List


class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		i = 0
		k = 1
		minSubarray = 0
		n = len(nums) - 1
		currentSum = nums[0]
		growing = True
		if currentSum >= target:
			minSubarray = 1
		while k <= n:
			if growing:
				currentSum += nums[k]
			else:
				currentSum -= nums[i - 1]
			if currentSum < target:
				k += 1
				growing = True

			else:
				minSubarray = min(minSubarray, k - i + 1) if minSubarray else k - i + 1
				i += 1
				growing = False

		return minSubarray


if __name__ == "__main__":
	sol = Solution()
	target = 6
	nums = [10, 2, 3]
	# target = 7
	# nums = [2, 3, 1, 2, 4, 3]
	print(sol.minSubArrayLen(target, nums))
