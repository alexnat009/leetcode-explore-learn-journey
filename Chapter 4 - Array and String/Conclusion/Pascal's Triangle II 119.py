import math
from typing import List


class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		return [self.binomial_coefficient(rowIndex, i) for i in range(rowIndex + 1)]

	def binomial_coefficient(self, n, k):
		return math.comb(n, k)


if __name__ == "__main__":
	sol = Solution()

	k = 7

	print(sol.getRow(k))
