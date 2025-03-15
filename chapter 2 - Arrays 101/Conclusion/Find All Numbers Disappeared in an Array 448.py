from collections import Counter
from typing import List


class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		res = []
		cnt = Counter(nums)
		for i in range(1, len(nums) + 1):
			if not cnt.get(i):
				res.append(i)
		return res


if __name__ == "__main__":
	sol = Solution()
	nums = [4, 3, 2, 7, 8, 2, 3, 1]
	# nums = [1, 1]
	print(sol.findDisappearedNumbers(nums))
	print(nums)
