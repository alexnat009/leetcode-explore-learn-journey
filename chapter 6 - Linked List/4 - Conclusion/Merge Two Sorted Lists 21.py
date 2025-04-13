from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0)
		tail = dummy

		while list1 and list2:
			if list1.val < list2.val:
				tail.next = list1
				list1 = list1.next
			else:
				tail.next = list2
				list2 = list2.next
			tail = tail.next

		tail.next = list1 if list1 else list2

		return dummy.next


if __name__ == "__main__":
	sol = Solution()

	ls1 = create_linked_list_from_list([1, 2, 4])
	ls2 = create_linked_list_from_list([1, 3, 4])
	print_linked_list(sol.mergeTwoLists(ls1, ls2))
