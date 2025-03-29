from collections import deque
from typing import List


class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid:
			return 0

		n, m = len(grid), len(grid[0])
		visited = set()
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		island_count = 0

		def bfs(start_i, start_j):
			if not grid:
				return 0

			queue = deque([(start_i, start_j)])
			visited.add((start_i, start_j))

			while queue:
				current_i, current_j = queue.popleft()
				for di, dj in directions:
					next_i, next_j = current_i + di, current_j + dj
					if 0 <= next_i < n and 0 <= next_j < m and (next_i, next_j) not in visited and grid[next_i][
						next_j] == "1":
						queue.append((next_i, next_j))
						visited.add((next_i, next_j))

		for i in range(n):
			for j in range(m):
				if grid[i][j] == "1" and (i, j) not in visited:
					bfs(i, j)
					island_count += 1

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
