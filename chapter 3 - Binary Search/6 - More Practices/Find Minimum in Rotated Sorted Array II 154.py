from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2
			if nums[mid] == nums[high]:
				high -= 1
			elif nums[mid] < nums[high]:
				high = mid
			else:
				low = mid + 1
		return nums[low]

	def rotate_n_times(self, arr, n):
		n %= len(arr)
		if n == 0:
			return arr

		return arr[-n:] + arr[:-n]


if __name__ == "__main__":
	sol = Solution()

	# nums = [1, 3, 3, 3]
	nums = [2, 2, 2]

	# numsPvt = sol.rotate_n_times(nums, 0)
	# print(numsPvt)

	print(sol.findMin(nums))
