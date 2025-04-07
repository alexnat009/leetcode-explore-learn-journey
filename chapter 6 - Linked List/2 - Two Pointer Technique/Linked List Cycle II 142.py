from typing import Optional

from utils.utils import ListNode


class Solution:
	def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		try:
			ptrSlow = head
			ptrFast = head
			while True:
				ptrSlow = ptrSlow.next
				ptrFast = ptrFast.next.next
				if ptrSlow == ptrFast:
					break
			ptrSlow = head
			while ptrSlow != ptrFast:
				ptrSlow = ptrSlow.next
				ptrFast = ptrFast.next
			return ptrSlow
		except AttributeError:
			return None


if __name__ == "__main__":
	sol = Solution()
	head = [3, 2, 0, -4]
	pos = 1
