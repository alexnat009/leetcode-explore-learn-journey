from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		idx = 1
		for i in range(len(nums) - 1):
			if nums[i] != nums[i + 1]:
				nums[idx] = nums[i + 1]
				idx += 1
		return idx

if __name__ == "__main__":
	sol = Solution()
	nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	# nums = [0, 1, 1, 2, 2, 4, 4, 7, 8, 9, 10, 10]
	# nums = []
	print(sol.removeDuplicates(nums))
	print(nums)
