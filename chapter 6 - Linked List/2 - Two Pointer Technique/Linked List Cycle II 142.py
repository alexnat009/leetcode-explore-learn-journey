from typing import Optional

from utils.utils import ListNode


class Solution:
	def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head:
			return None

		ptr = head
		visited = {head}
		while ptr and ptr.next:
			ptr = ptr.next
			if ptr in visited:
				return ptr
			visited.add(ptr)
		return None


if __name__ == "__main__":
	sol = Solution()
	head = [3, 2, 0, -4]
	pos = 1

