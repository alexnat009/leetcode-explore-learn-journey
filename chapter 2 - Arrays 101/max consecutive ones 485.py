from typing import List


class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		maxSum = 0
		currentSum = 0
		for i in nums:
			if i == 1:
				currentSum += 1
			else:
				maxSum = max(maxSum, currentSum)
				currentSum = 0
		return max(maxSum, currentSum)


if __name__ == "__main__":
	sol = Solution()
	nums = [1, 1, 0, 1, 1, 1]

	print(sol.findMaxConsecutiveOnes(nums))
