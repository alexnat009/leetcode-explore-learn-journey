class ListNode:
	def __init__(self, val, prev_node=None, next_node=None):
		self.val = val
		self.prev = prev_node
		self.next = next_node


class MyLinkedList:

	def __init__(self):
		self.left = ListNode(0)
		self.right = ListNode(0)
		self.left.next = self.right
		self.right.prev = self.left

	def get(self, index: int) -> int:
		cur = self.left.next
		while cur and index > 0:
			cur = cur.next
			index -= 1
		return cur.val if (cur and cur != self.right and index == 0) else -1

	def addAtHead(self, val: int) -> None:
		node = ListNode(val, self.left, self.left.next)
		self.left.next.prev = node
		self.left.next = node

	def addAtTail(self, val: int) -> None:
		node = ListNode(val, self.right.prev, self.right)
		self.right.prev.next = node
		self.right.prev = node

	def addAtIndex(self, index: int, val: int) -> None:
		cur = self.left.next
		while cur and index > 0:
			cur = cur.next
			index -= 1
		if cur and index == 0:
			node = ListNode(val, cur.prev, cur)
			cur.prev.next = node
			cur.prev = node

	def deleteAtIndex(self, index: int) -> None:
		cur = self.left.next
		while cur and index > 0:
			cur = cur.next
			index -= 1
		if cur and cur != self.right and index == 0:
			cur.next.prev = cur.prev
			cur.prev.next = cur.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
