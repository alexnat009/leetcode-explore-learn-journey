from collections import deque
from typing import List


class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		queue = deque([*rooms[0]])
		visited = {0}
		while queue:
			step = queue.popleft()
			if step not in visited:
				visited.add(step)
				queue.extend(rooms[step])
		return True if len(rooms) == len(visited) else False


if __name__ == "__main__":
	sol = Solution()
	rooms = [[1], [2], [3], []]
	rooms = [[1, 3], [3, 0, 1], [2], [0]]
	print(sol.canVisitAllRooms(rooms))
