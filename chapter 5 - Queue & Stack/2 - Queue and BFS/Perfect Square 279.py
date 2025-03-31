from collections import deque


class Solution:
	def numSquares(self, n: int) -> int:
		def plusSquare(root, upperLimit):
			i = 1
			while True:
				nextNum = root + i ** 2
				if nextNum > upperLimit:
					return  # Stop the generator
				yield nextNum
				i += 1  # Move to the next square

		root = 0
		queue = deque([(root, 0)])
		visited = {root}

		while queue:

			current, step = queue.popleft()
			for nextNum in plusSquare(current, upperLimit=n):
				if nextNum:
					if nextNum not in visited:
						if nextNum == n:
							return step + 1
						queue.append((nextNum, step + 1))
						visited.add(nextNum)
		return -1


if __name__ == "__main__":
	sol = Solution()
	n = 13
	print(sol.numSquares(n))
