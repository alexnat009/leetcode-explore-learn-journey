from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		if not matrix or not matrix[0]:
			return []
		rows = len(matrix)
		cols = len(matrix[0])
		res = []

		cols_visited_left = cols_visited_right = 0
		rows_visited_upper = 1
		rows_visited_lower = 0
		cur_col = cur_row = 0
		direction = 'right'

		while len(res) != rows * cols:
			res.append(matrix[cur_row][cur_col])
			match direction:
				case 'right':
					if cur_col < cols - cols_visited_left - 1:
						cur_col += 1
					else:
						direction = 'down'
						cols_visited_right += 1
						cur_row += 1

				case 'down':
					if cur_row < rows - rows_visited_lower - 1:
						cur_row += 1
					else:
						direction = 'left'
						rows_visited_lower += 1
						cur_col -= 1

				case 'left':
					if cur_col > cols_visited_right - 1:
						cur_col -= 1
					else:
						direction = 'up'
						cols_visited_left += 1
						cur_row -= 1

				case 'up':
					if cur_row > rows_visited_upper:
						cur_row -= 1
					else:
						direction = 'right'
						rows_visited_upper += 1
						cur_col += 1

		return res


if __name__ == "__main__":
	sol = Solution()

	matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
	# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	# matrix = [[3], [2]]
	print(sol.spiralOrder(matrix))
