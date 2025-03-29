from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		k = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[i], nums[k] = nums[k], nums[i]
				k += 1


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 0, 3, 12]
	# nums = [1, 2, 0, 3, 0]
	sol.moveZeroes(nums)
	print(nums)
