from collections import deque
from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


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
