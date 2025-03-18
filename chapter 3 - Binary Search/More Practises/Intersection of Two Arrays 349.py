from typing import List


class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1 = set(nums1)
		nums2 = set(nums2)
		return list(nums1.intersection(nums2))


if __name__ == "__main__":
	sol = Solution()

	nums1 = [1, 2, 2, 1]
	nums2 = [2, 2]

	print(sol.intersection(nums1, nums2))
