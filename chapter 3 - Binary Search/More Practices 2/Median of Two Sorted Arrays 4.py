from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if len(nums1) > len(nums2):
			return self.findMedianSortedArrays(nums2, nums1)

		n, m = len(nums1), len(nums2)
		total = n + m
		half = total // 2

		low = 0
		high = n
		while low <= high:
			smallNumsMidIdx = low + (high - low) // 2
			longNumsMidIdx = half - smallNumsMidIdx

			smallNumsLeft = nums1[smallNumsMidIdx - 1] if smallNumsMidIdx > 0 else float("-inf")
			smallNumsRight = nums1[smallNumsMidIdx] if smallNumsMidIdx < n else float("inf")

			longNumsLeft = nums2[longNumsMidIdx - 1] if longNumsMidIdx > 0 else float("-inf")
			longNumsRight = nums2[longNumsMidIdx] if longNumsMidIdx < m else float("inf")

			if smallNumsLeft <= longNumsRight and longNumsLeft <= smallNumsRight:
				if total % 2 == 0:
					return (max(smallNumsLeft, longNumsLeft) + min(smallNumsRight, longNumsRight)) / 2
				else:
					return min(smallNumsRight, longNumsRight)
			elif smallNumsLeft > longNumsRight:
				high = smallNumsMidIdx - 1
			else:
				low = smallNumsMidIdx + 1


if __name__ == "__main__":
	sol = Solution()


	nums1 = [1, 2, 3, 4, 4, 5]
	nums2 = [1, 2, 3, 4, 5]
	print(sol.findMedianSortedArrays(nums1, nums2))
