from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low <= high:
			mid = low + (high - low) // 2
			if nums[mid] == target:
				return mid
			if nums[low] <= nums[mid]:
				if nums[low] <= target <= nums[mid]:
					high = mid
				else:
					low = mid + 1
			else:
				if nums[mid] <= target <= nums[high]:
					low = mid + 1
				else:
					high = mid
		return -1

	def pivot_array(self, arr, pivot_index):
		return arr[pivot_index:] + arr[:pivot_index]


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 2, 4, 5, 6, 7]
	target = 0
	pvt = 3
	numsPvt = sol.pivot_array(nums, pvt)
	print(f'nums={numsPvt}, pvt={pvt}, looking for {target}, found at {sol.search(numsPvt, target)}')
