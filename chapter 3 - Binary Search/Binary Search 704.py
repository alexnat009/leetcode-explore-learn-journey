from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		return [
			self.search_left(nums, target),
			self.search_right(nums, target),
			self.search_some(nums, target)
		]

	def search_left(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low) // 2
			# mid = (low + high) >> 1
			if nums[mid] < target:
				low = mid + 1
			else:
				high = mid

		return low if nums[low] == target else -1

	def search_right(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high - low + 1) // 2
			# mid = (low + high + 1) >> 1
			if nums[mid] > target:
				high = mid - 1
			else:
				low = mid
		return low if nums[low] == target else -1

	def search_some(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return -1


if __name__ == "__main__":
	sol = Solution()
	nums = [9, 9, 9, 9, 9, 9, 9]
	target = 9
	print(sol.search(nums, target))
