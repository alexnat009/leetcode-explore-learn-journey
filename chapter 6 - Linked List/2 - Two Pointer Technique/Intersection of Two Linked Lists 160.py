from typing import Optional

from utils.utils import ListNode


class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
		visited = set()

		ptrA = headA
		while ptrA:
			visited.add(ptrA)
			ptrA = ptrA.next
		ptrB = headB
		while ptrB:
			if ptrB in visited:
				return ptrB
			ptrB = ptrB.next
		return None
