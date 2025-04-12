from typing import Optional

from utils.utils import ListNode


class Solution:
	def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
		tmp = ListNode()
		tmp1 = tmp
		while head:
			if head.val != val:
				tmp1.next = head
				tmp1 = tmp1.next
			head = head.next
		tmp1.next = None
		return tmp.next

