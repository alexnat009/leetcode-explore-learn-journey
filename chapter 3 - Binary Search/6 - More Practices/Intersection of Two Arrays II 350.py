from typing import List
from collections import Counter


class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		if not nums1 or not nums2:
			return []
		nums1.sort()
		nums2.sort()
		n1, n2, p1, p2 = len(nums1), len(nums2), 0, 0
		res = []

		while p1 < n1 and p2 < n2:
			if nums1[p1] == nums2[p2]:
				res.append(nums1[p1])
				p1 += 1
				p2 += 1
			elif nums1[p1] < nums2[p2]:
				p1 += 1
			else:
				p2 += 1
		return res


if __name__ == "__main__":
	sol = Solution()

	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2, 1]

	print(sol.intersect(nums1, nums2))
