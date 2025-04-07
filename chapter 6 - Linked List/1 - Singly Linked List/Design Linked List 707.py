class ListNode:
	def __init__(self, val, next_node=None):
		self.val = val
		self.next = next_node


class MyLinkedList:

	def __init__(self):
		self.left = ListNode(0)
		self.right = ListNode(0)
		self.left.next = self.right
		self.size = 0

	def get(self, index: int) -> int:
		if index < 0 or index >= self.size:
			return -1
		cur = self.left.next
		while index > 0:
			cur = cur.next
			index -= 1
		return cur.val

	def addAtHead(self, val: int) -> None:
		node = ListNode(val, self.left.next)
		self.left.next = node
		self.size += 1

	def addAtTail(self, val: int) -> None:
		cur = self.left
		while cur.next != self.right:
			cur = cur.next
		node = ListNode(val, self.right)
		cur.next = node
		self.size += 1

	def addAtIndex(self, index: int, val: int) -> None:
		if index < 0 or index > self.size:
			return
		cur = self.left
		while index > 0:
			cur = cur.next
			index -= 1
		new_node = ListNode(val, cur.next)
		cur.next = new_node
		self.size += 1

	def deleteAtIndex(self, index: int) -> None:
		if index < 0 or index >= self.size:
			return
		cur = self.left
		while index > 0:
			cur = cur.next
			index -= 1
		cur.next = cur.next.next
		self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
