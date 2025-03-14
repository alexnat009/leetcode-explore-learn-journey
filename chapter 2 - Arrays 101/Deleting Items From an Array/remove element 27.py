from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		lastId = len(nums) - 1
		currentId = len(nums) - 1
		while currentId >= 0:
			if nums[currentId] == val:
				nums[lastId], nums[currentId] = nums[currentId], nums[lastId]
				lastId -= 1
			currentId -= 1
		return lastId + 1


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 2, 2, 3, 0, 4, 2, 5, 2]
	val = 2
	print(sol.removeElement(nums, val))
	print(nums)
