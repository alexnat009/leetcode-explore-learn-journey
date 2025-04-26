from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if not head or k == 0:
			return head

		length = 1
		tail = head
		while tail.next:
			tail = tail.next
			length += 1

		k = k % length
		if k == 0:
			return head

		new_tail = head
		for _ in range(length - k - 1):
			new_tail = new_tail.next

		new_head = new_tail.next
		new_tail.next = None
		tail.next = head
		return new_head


if __name__ == "__main__":
	sol = Solution()

	ls = create_linked_list_from_list([0, 1, 2, 3, 4])
	print_linked_list(sol.rotateRight(ls, 3))
