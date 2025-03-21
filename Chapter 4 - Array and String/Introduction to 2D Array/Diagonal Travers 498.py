from typing import List
import numpy as np


class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		rows = len(mat)
		cols = len(mat[0])
		res = []
		cur_col = cur_row = 0
		going_up = True

		while len(res) != rows * cols:
			if going_up:
				while cur_row >= 0 and cur_col < cols:
					res.append(mat[cur_row][cur_col])

					cur_row -= 1
					cur_col += 1
				if cur_col == cols:
					cur_col -= 1
					cur_row += 2
				else:
					cur_row += 1
				going_up = False
			else:
				while cur_col >= 0 and cur_row < rows:
					res.append(mat[cur_row][cur_col])

					cur_row += 1
					cur_col -= 1
				if cur_row == rows:
					cur_col += 2
					cur_row -= 1
				else:
					cur_col += 1
				going_up = True
		return res


if __name__ == "__main__":
	sol = Solution()

	mat = [[1, 2, 3], [4, 5, 6]]
	mat1 = np.ones((3, 5), dtype=np.int_)
	print(sol.findDiagonalOrder(mat))
