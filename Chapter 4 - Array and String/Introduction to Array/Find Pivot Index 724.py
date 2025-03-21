from typing import List


class Solution:
	def pivotIndex(self, nums: List[int]) -> int:
		leftSum, rightSum = 0, sum(nums)
		for idx, num in enumerate(nums):
			rightSum -= num

			if leftSum == rightSum:
				return idx

			leftSum += num

		return -1


if __name__ == "__main__":
	sol = Solution()

	nums = [1, 7, 3, 6, 5, 6]
	print(sol.pivotIndex(nums))
