import pprint
from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		if not head or not head.next:
			return True

		slow, fast = head, head
		prev = None

		while fast and fast.next:
			fast = fast.next.next
			next_node = slow.next
			slow.next = prev
			prev = slow
			slow = next_node
		if fast:
			slow = slow.next
		while prev and slow:
			if prev.val != slow.val:
				return False
			slow = slow.next
			prev = prev.next
		return True


if __name__ == "__main__":
	sol = Solution()

	ls = create_linked_list_from_list([1, 1, 3, 1, 1])
	print_linked_list(ls)
	print(sol.isPalindrome(ls))
