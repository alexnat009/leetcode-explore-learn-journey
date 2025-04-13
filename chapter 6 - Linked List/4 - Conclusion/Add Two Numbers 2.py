from copyreg import remove_extension
from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0)
		cur = dummy

		carry = 0
		while l1 or l2 or carry:
			v1 = l1.val if l1 else 0
			v2 = l2.val if l2 else 0
			val = v1 + v2 + carry

			val, carry = val % 10, val // 10
			cur.next = ListNode(val)

			cur = cur.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None

		return dummy.next


if __name__ == "__main__":
	sol = Solution()
	ls1 = create_linked_list_from_list([1, 2, 6, 9])
	ls2 = create_linked_list_from_list([1, 4, 5, 8])

	print_linked_list(sol.addTwoNumbers(ls1, ls2))
