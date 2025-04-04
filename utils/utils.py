from collections import deque
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Node:
	def __init__(self, val):
		self.val = val
		self.neighbors = []  #


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# Helper function to create a linked list from a list of values
def create_linked_list_from_list(values):
	if not values:
		return None
	head = ListNode(values[0])
	current = head
	for val in values[1:]:
		current.next = ListNode(val)
		current = current.next
	return head


# Helper function to print a linked list
def print_linked_list(head):
	values = []
	while head:
		values.append(str(head.val))
		head = head.next
	print(" -> ".join(values))


def print_tree(root: Optional[TreeNode]):
	if not root:
		print("Tree is empty")
		return

	queue = deque([root])
	result = []

	while queue:
		node = queue.popleft()
		if node:
			result.append(str(node.val))
			queue.append(node.left)
			queue.append(node.right)
		else:
			result.append("None")

	# Remove trailing "None" values
	while result and result[-1] == "None":
		result.pop()

	print(" ".join(result))


def bfs_no_visited_hash(root: Node, target: Node):
	if root == target:
		return 0
	queue = deque([root])
	step = 0

	while queue:
		size = len(queue)
		for _ in range(size):
			cur = queue.popleft()
			if cur == target:
				return step
			for neighbor in cur.neighbors:
				queue.append(neighbor)
		step += 1
	return -1


def bfs_visited_hash(root: Node, target: Node):
	if root == target:
		return 0
	queue = deque([root])
	visited = {root}
	step = 0

	while queue:
		size = len(queue)
		for _ in range(size):
			cur = queue.popleft()
			if cur == target:
				return step
			for neighbor in cur.neighbors:
				if neighbor not in visited:
					queue.append(neighbor)
					visited.add(neighbor)
		step += 1
	return -1


def dfs_recursive(cur: Node, target: Node, visited: set):
	if cur == target:
		return True

	for next_node in cur.neighbors:
		if next_node not in visited:
			visited.add(next_node)
			if dfs_recursive(next_node, target, visited):
				return True
	return False


def dfs_iterative(cur: Node, target: Node, visited: set):
	stack = deque([cur])
	visited.add(cur)
	while stack:
		cur = deque.popleft()
		if cur == target:
			return True
		for neighbor in cur.neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				stack.append(visited)
	return False
