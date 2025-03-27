from typing import List


class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		n = len(nums)

		prefixSum = [0] * (n + 1)
		for i in range(1, n + 1):
			prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

		left, right = 1, n
		result = n + 1

		while left <= right:
			mid = (left + right) // 2
			if self.isValid(prefixSum, mid):
				result = mid
				right = mid - 1
			else:
				left = mid + 1

		return result if result != n + 1 else 0

	def isValid(self, prefixSum: List[int], length: int) -> bool:
		for start in range(len(prefixSum) - length):
			end = start + length
			if prefixSum[end] - prefixSum[start] >= target:
				return True
		return False


if __name__ == "__main__":
	sol = Solution()
	# target = 6
	# nums = [10, 2, 3]
	target = 7
	nums = [2, 3, 1, 2, 4, 3]
	print(sol.minSubArrayLen(target, nums))
