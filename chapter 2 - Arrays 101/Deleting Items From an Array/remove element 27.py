from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		j = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[j] = nums[i]
				j += 1
		return j


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 2, 2, 3, 0, 4, 2, 5, 2]
	val = 2
	print(sol.removeElement(nums, val))
	print(nums)
