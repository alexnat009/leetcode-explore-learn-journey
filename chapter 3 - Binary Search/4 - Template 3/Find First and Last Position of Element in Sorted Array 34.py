from typing import List


class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		if not nums:
			return [-1, -1]

		left = self.search_boundary(nums, target, is_left=True)
		if left == -1:
			return [-1, -1]
		right = self.search_boundary(nums, target, is_left=False)
		return [left, right]

	def search_boundary(self, nums: List[int], target: int, is_left=True) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			if is_left:
				mid = low + (high - low) // 2

				if nums[mid] < target:
					low = mid + 1
				else:
					high = mid
			else:
				mid = low + (high - low + 1) // 2
				if nums[mid] > target:
					high = mid - 1
				else:
					low = mid

		return low if nums[low] == target else -1


if __name__ == "__main__":
	sol = Solution()
	nums = [5, 7, 7, 8, 8, 8, 8, 8, 10]
	target = 8
	print(sol.searchRange(nums, target))
