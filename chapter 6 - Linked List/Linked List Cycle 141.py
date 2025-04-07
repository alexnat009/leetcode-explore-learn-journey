# Definition for singly-linked list.


from typing import Optional

from utils.utils import ListNode


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		try:
			ptrSlow = head
			ptrFast = head.next
			while ptrSlow is not ptrFast:
				ptrSlow = ptrSlow.next
				ptrFast = ptrFast.next.next
			return True
		except AttributeError:
			return False


if __name__ == "__main__":
	sol = Solution()

	head = [3, 2, 0, -4]
	pos = 1
