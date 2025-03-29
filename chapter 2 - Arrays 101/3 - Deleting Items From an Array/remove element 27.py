from typing import List


class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		n = len(nums)
		slowP = 0
		fastP = 0
		while fastP < n:
			if nums[slowP] != val:
				slowP += 1
				fastP += 1
			else:
				if nums[fastP] != val:
					nums[fastP], nums[slowP] = nums[slowP], nums[fastP]
					slowP += 1
				fastP += 1
		return slowP


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 2, 2, 3, 0, 4, 2, 5, 2]
	val = 2
	print(sol.removeElement(nums, val))
	print(nums)
