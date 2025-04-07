from typing import Optional

from utils.utils import ListNode


class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
		ptrA = headA
		ptrB = headB
		while ptrA != ptrB:
			ptrA = ptrA.next if ptrA else headB
			ptrB = ptrB.next if ptrB else headA

		return ptrA
