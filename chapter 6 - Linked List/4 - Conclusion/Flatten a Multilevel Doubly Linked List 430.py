from typing import Optional


class Node:
	def __init__(self, val, prev=None, next=None, child=None):
		self.val = val
		self.prev = prev
		self.next = next
		self.child = child


class Solution:
	def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
		if not head:
			return None

		dummy = Node(0)
		curr = dummy
		stack = [head]

		while stack:
			node = stack.pop()

			if node.next:
				stack.append(node.next)
			if node.child:
				stack.append(node.child)

			curr.next = node
			node.prev = curr
			node.child = None
			curr = node

		dummy.next.prev = None
		return dummy.next
