from typing import List


class Solution:
	def splitArray(self, nums: List[int], k: int) -> int:
		low = max(nums)
		high = sum(nums)
		res = high
		while low <= high:
			mid = low + (high - low) // 2
			if self.canSplit(nums, mid, k):
				res = mid
				high = mid - 1
			else:
				low = mid + 1
		return low

	def canSplit(self, nums, largest, numberOfSubArrays):
		subArray = 0
		currentSum = 0
		for n in nums:
			currentSum += n
			if currentSum > largest:
				subArray += 1
				currentSum = n
		return subArray + 1 <= numberOfSubArrays


if __name__ == "__main__":
	sol = Solution()

	nums = [7, 2, 5, 10, 18]
	k = 3
	print(sol.splitArray(nums, k))
