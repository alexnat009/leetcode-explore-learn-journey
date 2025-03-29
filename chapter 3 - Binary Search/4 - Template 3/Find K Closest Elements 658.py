from typing import List


class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		if x <= arr[0]:
			return arr[:k]
		if x >= arr[-1]:
			return arr[-k:]

		low = 0
		high = len(arr) - k
		while low < high:
			mid = low + (high - low) // 2
			if x - arr[mid] > arr[mid + k] - x:
				low = mid + 1
			else:
				high = mid
		return arr[low:low + k]


if __name__ == "__main__":
	sol = Solution()

	arr = [1, 1, 2, 3, 3, 4, 5, 8]
	k = 4
	x = 3
	print(sol.findClosestElements(arr, k, x))
