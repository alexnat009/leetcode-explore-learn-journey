from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2
			if nums[mid] > nums[high]:
				low = mid + 1
			else:
				high = mid
		return nums[low]

	def rotate_n_times(self, arr, n):
		n %= len(arr)
		if n == 0:
			return arr

		return arr[-n:] + arr[:-n]


if __name__ == "__main__":
	sol = Solution()

	nums = [1, 2, 4, 5, 6, 7]

	numsPvt = sol.rotate_n_times(nums, 4)
	print(sol.findMin(numsPvt))
