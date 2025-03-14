import math
from typing import List


class Solution:
	def findNumbers(self, nums: List[int]) -> int:
		return sum(1 for i in nums if len(str(i)) % 2 == 0)


if __name__ == "__main__":
	sol = Solution()
	nums = [12, 345, 2, 6, 7896]

	print(sol.findNumbers(nums))
