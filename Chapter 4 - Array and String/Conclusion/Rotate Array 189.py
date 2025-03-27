from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		k %= len(nums)
		if k:
			nums[:] = nums[-k:] + nums[:-k]
		else:
			pass


if __name__ == "__main__":
	sol = Solution()
	# nums = [10, 2, 3]

	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	# nums = [-1, -100, 3, 99]
	# k = 2
	# nums = [1]
	# k = 0
	# nums = [1]
	# k = 1
	print(sol.rotate(nums, k))
	print(nums)
