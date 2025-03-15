from typing import List


class Solution:
	def sortArrayByParity(self, nums: List[int]) -> List[int]:

		k = 0
		for i in range(len(nums)):
			if nums[i] % 2 == 0:
				nums[i], nums[k] = nums[k], nums[i]
				k += 1
		return nums


if __name__ == "__main__":
	sol = Solution()
	nums = [3, 1, 2, 4, 1, 1, 4, 6, 7, 2, 72, 1, 3, 7]
	# nums = [1, 2, 0, 3, 0]
	sol.sortArrayByParity(nums)
	print(nums)
