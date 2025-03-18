from typing import List
from collections import Counter


class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		cnt1 = Counter(nums1)
		cnt2 = Counter(nums2)
		res = []
		for key, value in (cnt1 & cnt2).items():
			res.extend([key for _ in range(value)])
		return res


if __name__ == "__main__":
	sol = Solution()

	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2]

	print(sol.intersect(nums1, nums2))
