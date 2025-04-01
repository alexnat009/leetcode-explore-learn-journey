from collections import deque
from typing import List


class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0

		n, m = len(grid), len(grid[0])
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		island_count = 0

		def dfs(start_i, start_j):
			if start_i < 0 or start_j < 0 or start_i >= n or start_j >= m or grid[start_i][start_j] != "1":
				return

			grid[start_i][start_j] = "0"

			for di, dj in directions:
				dfs(start_i + di, start_j + dj)

		for i in range(n):
			for j in range(m):
				if grid[i][j] == "1":
					island_count += 1
					dfs(i, j)

		return island_count


# print(visited)


if __name__ == "__main__":
	sol = Solution()

	grid = [
		["0", "1", "0", "0", "0"],
		["1", "1", "0", "0", "0"],
		["0", "0", "1", "0", "0"],
		["1", "0", "0", "1", "1"]
	]

	print(sol.numIslands(grid))
