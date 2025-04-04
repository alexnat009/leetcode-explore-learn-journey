from collections import deque
from typing import List


class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
		if image[sr][sc] == color:
			return image

		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		original_color = image[sr][sc]
		image[sr][sc] = color
		queue = deque([(sr, sc)])

		n, m = len(image), len(image[0])
		while queue:
			(x, y) = queue.popleft()
			image[x][y] = color
			for dx, dy in directions:
				if 0 <= x + dx < n and 0 <= y + dy < m and image[x + dx][y + dy] == original_color:
					queue.append((x + dx, y + dy))
		return image


if __name__ == "__main__":
	sol = Solution()
	image = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
	sr = 1
	sc = 1
	color = 2

	# print(sol.floodFill(image, sr, sc, color))
	tmp = sol.floodFill(image, sr, sc, color)
	for i in tmp:
		for j in i:
			print(j, end=" ")
		print()
