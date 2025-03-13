from typing import Optional

from utils.utils import ListNode, create_linked_list_from_list, print_linked_list


class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head:
			return None
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow


if __name__ == "__main__":
	values = [1, 2, 3, 4, 5]  # Change this list to test different cases
	head = create_linked_list_from_list(values)

	print("Original Linked List:")
	print_linked_list(head)

	solution = Solution()
	middle = solution.middleNode(head)

	print("\nMiddle Node and following nodes:")
	print_linked_list(middle)
