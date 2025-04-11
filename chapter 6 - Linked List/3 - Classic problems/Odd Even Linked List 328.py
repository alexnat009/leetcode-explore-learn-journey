from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head or not head.next:
			return head

		odd = head
		even = head.next
		evenStartNode = head.next
		while odd and even and odd.next and even.next:
			odd.next = even.next
			odd = even.next
			even.next = odd.next
			even = odd.next

		odd.next = evenStartNode
		return head


if __name__ == "__main__":
	sol = Solution()

	ls = create_linked_list_from_list([1, 2, 3, 4, 5, 6])
	print(print_linked_list(sol.oddEvenList(ls)))
