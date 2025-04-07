from typing import Optional

from utils.utils import ListNode


class Solution:
	def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head or not head.next:
			return None

		ptrSlow = head
		ptrFast = head
		while ptrFast and ptrFast.next:
			ptrSlow = ptrSlow.next
			ptrFast = ptrFast.next.next
			if ptrFast == ptrSlow:
				break
		else:
			return None
		ptrSlow = head
		while ptrFast != ptrSlow:
			ptrSlow = ptrSlow.next
			ptrFast = ptrFast.next
		return ptrSlow


if __name__ == "__main__":
	sol = Solution()
	head = [3, 2, 0, -4]
	pos = 1
