from typing import List


class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		arr = sorted(arr)
		for i in range(len(arr)):
			target = arr[i] * 2
			if self.binarySearch(arr, target, i):
				return True
		return False

	def binarySearch(self, arr: List[int], target: int, exclude_index: int) -> int:
		left = 0
		right = len(arr) - 1
		while left <= right:
			mid = left + (right - left) // 2

			if arr[mid] == target and mid != exclude_index:
				return True
			elif arr[mid] < target:
				left = mid + 1
			else:
				right = mid - 1
		return False


if __name__ == "__main__":
	sol = Solution()
	arr = [-2, 0, 10, -19, 4, 6, -8]

	print(sol.checkIfExist(arr))
