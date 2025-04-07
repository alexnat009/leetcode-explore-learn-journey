# Definition for singly-linked list.


from typing import Optional

from utils.utils import ListNode


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		if not head:
			return False
		ptrSlow = head
		ptrFast = head

		while ptrFast.next and ptrFast.next.next:
			ptrSlow = ptrSlow.next
			ptrFast = ptrFast.next.next
			if ptrSlow == ptrFast:
				return True
		return False


if __name__ == "__main__":
	sol = Solution()

	head = [3, 2, 0, -4]
	pos = 1
