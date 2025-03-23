from typing import List


class Solution:

	def generate(self, numRows: int) -> List[List[int]]:
		res = [[1] * (i + 1) for i in range(numRows)]

		for i in range(2, numRows):
			for k in range(1, i):
				res[i][k] = res[i - 1][k - 1] + res[i - 1][k]
		return res


if __name__ == "__main__":
	sol = Solution()
	numRows = 5
	print(sol.generate(numRows))
