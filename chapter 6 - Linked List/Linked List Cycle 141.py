# Definition for singly-linked list.


from typing import Optional

from utils.utils import ListNode


class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		if not head:
			return False
		ptr = head
		visited = {ptr}

		while ptr.next:
			ptr = ptr.next
			if ptr in visited:
				return True
			else:
				visited.add(ptr)
		return False


if __name__ == "__main__":
	sol = Solution()

	head = [3, 2, 0, -4]
	pos = 1
