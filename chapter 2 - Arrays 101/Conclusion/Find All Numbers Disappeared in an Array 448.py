from collections import Counter
from typing import List


class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		for num in nums:
			i = abs(num) - 1
			nums[i] = -1 * abs(nums[i])
		res = []
		for i, n in enumerate(nums):
			if n > 0:
				res.append(i + 1)
		return res

if __name__ == "__main__":
	sol = Solution()
	nums = [1, 5, 4, 5, 5]
	print(sol.findDisappearedNumbers(nums))
	print(nums)
