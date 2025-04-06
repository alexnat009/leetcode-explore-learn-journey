import pprint
from collections import deque
from typing import List


class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		n = len(mat)
		m = len(mat[0])
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

		res = [[float('inf')] * m for _ in range(n)]
		queue = deque()
		for i in range(n):
			for j in range(m):
				if mat[i][j] == 0:
					res[i][j] = 0
					queue.append((i, j))
		while queue:
			x, y = queue.popleft()
			for dx, dy in directions:
				nx, ny = x + dx, y + dy
				if 0 <= nx < n and 0 <= ny < m:
					if res[nx][ny] > res[x][y] + 1:
						res[nx][ny] = res[x][y] + 1
						queue.append((nx, ny))
		return res


if __name__ == "__main__":
	sol = Solution()
	# mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
	# mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
	mat = [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
		   [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
		   [1, 1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
		   [1, 0, 1, 1, 1, 0, 1, 1, 1, 0]]
	pprint.pprint(sol.updateMatrix(mat))
