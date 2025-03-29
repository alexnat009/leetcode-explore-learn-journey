from typing import List


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		idSum = m + n - 1
		while n > 0:
			if m > 0 and nums1[m - 1] >= nums2[n - 1]:
				nums1[idSum] = nums1[m - 1]
				m -= 1
			else:
				nums1[idSum] = nums2[n - 1]
				n -= 1
			idSum -= 1


if __name__ == "__main__":
	sol = Solution()
	nums1 = [2, 2, 3, 0, 0, 0]
	m = 3
	nums2 = [1, 5, 6]
	n = 3
	sol.merge(nums1, m, nums2, n)
	print(nums1)
