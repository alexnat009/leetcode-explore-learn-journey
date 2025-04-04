from typing import List


class Solution:
	def findPeakElement(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2

			if nums[mid] > nums[mid + 1]:
				high = mid
			else:
				low = mid + 1
		return low


if __name__ == "__main__":
	sol = Solution()
	nums = [1, 2, 3, 4]
	print(sol.findPeakElement(nums))
