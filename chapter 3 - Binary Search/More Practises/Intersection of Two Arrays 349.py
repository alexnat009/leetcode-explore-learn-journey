from typing import List


class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		if not nums1 or not nums2:
			return []
		len1 = len(nums1)
		len2 = len(nums2)

		workingArray, searchArray = (nums1, nums2) if len1 >= len2 else (nums2, nums1)
		del len1, len2
		workingArray = sorted(workingArray)
		alreadyVisited = set()
		res = []
		for num in searchArray:
			low = 0
			high = len(workingArray) - 1
			if num in alreadyVisited:
				continue
			else:
				alreadyVisited.add(num)
			while low <= high:
				mid = low + (high - low) // 2
				if workingArray[mid] == num:
					res.append(workingArray[mid])
					break
				elif workingArray[mid] < num:
					low = mid + 1
				else:
					high = mid - 1
		return res


if __name__ == "__main__":
	sol = Solution()

	# nums1 = [1, 2, 2, 1]
	# nums2 = [2, 2, 1]
	nums1 = [4, 9, 5, 9, 8, 6]
	nums2 = [9, 4, 9, 8, 4]
	print(sol.intersection(nums1, nums2))
