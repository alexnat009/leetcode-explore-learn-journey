from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		n = len(nums)
		slowP = 0
		fastP = 1
		seenZero = False
		while fastP < n:
			if nums[fastP] != 0 and nums[slowP] != 0 and not seenZero:
				fastP += 1
				slowP += 1
			else:
				if nums[fastP] == 0:
					fastP += 1
					seenZero = True
				else:
					if nums[slowP] == 0:
						nums[slowP], nums[fastP] = nums[fastP], nums[slowP]
						seenZero = False
					slowP += 1


if __name__ == "__main__":
	sol = Solution()
	nums = [0, 1, 0, 3, 12]
	# nums = [1, 2, 0, 3, 0]
	sol.moveZeroes(nums)
	print(nums)
