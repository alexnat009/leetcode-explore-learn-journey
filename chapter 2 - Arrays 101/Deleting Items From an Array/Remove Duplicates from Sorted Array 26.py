from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		if not nums:
			return 0
		slowId = 0
		fastId = 0
		n = len(nums)
		while fastId < n:
			if nums[slowId] != nums[fastId]:
				slowId += 1
				nums[slowId] = nums[fastId]
			fastId += 1
		return slowId + 1


if __name__ == "__main__":
	sol = Solution()
	# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
	nums = [0, 1, 1, 2, 2, 4, 4, 7, 8, 9, 10, 10]
	# nums = []
	print(sol.removeDuplicates(nums))
	print(nums)
