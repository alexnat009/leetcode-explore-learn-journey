from typing import Optional


class Node:
	def __init__(self, val=0, neighbors=None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

	def __str__(self):
		# Create a string showing the node value and its neighbors' values
		neighbors_vals = [neighbor.val for neighbor in self.neighbors]
		return f"Node(val={self.val}, neighbors={neighbors_vals})"

	def __repr__(self):
		# Similar to __str__ to ensure it shows useful info in lists
		return self.__str__()


class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		visited = {}

		def dfs(node: Optional['Node']):
			if node in visited:
				return visited[node]

			copy = Node(node.val)
			visited[node] = copy
			for neighbor in node.neighbors:
				copy.neighbors.append(dfs(neighbor))
			return copy

		return dfs(node) if node else None


if __name__ == "__main__":
	nodes = [Node(i + 1) for i in range(4)]

	# Set up the adjacency list connections
	# Node 1 connects to nodes 2 and 4
	nodes[0].neighbors = [nodes[1], nodes[3]]
	# Node 2 connects to nodes 1 and 3
	nodes[1].neighbors = [nodes[0], nodes[2]]
	# Node 3 connects to nodes 2 and 4
	nodes[2].neighbors = [nodes[1], nodes[3]]
	# Node 4 connects to nodes 1 and 3
	nodes[3].neighbors = [nodes[0], nodes[2]]

	sol = Solution()
	cloned_node = sol.cloneGraph(nodes[0])

	print("Original nodes:")
	for node in nodes:
		print(node)

	print("\nCloned graph starting at cloned node:")

	# Use BFS to print all nodes in the cloned graph
	from collections import deque

	visited_set = set()
	queue = deque([cloned_node])
	visited_set.add(cloned_node)

	while queue:
		current = queue.popleft()
		print(current)
		for neighbor in current.neighbors:
			if neighbor not in visited_set:
				visited_set.add(neighbor)
				queue.append(neighbor)
