from typing import List


class Solution:
	def validMountainArray(self, arr: List[int]) -> bool:
		n = len(arr)
		if n < 3:
			return False

		idx = -1

		for i in range(n - 1):
			if arr[i] >= arr[i + 1]:
				idx = i
				break

		if idx == 0:
			return False

		for i in range(idx, n - 1):
			if arr[i] <= arr[i + 1]:
				return False

		return True


if __name__ == "__main__":
	sol = Solution()
	arr = [1, 2, 3, 4, 5]
	# arr = [2, 0, 2]
	# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	# arr = [1, 7, 9, 5, 4, 1, 2]
	arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	print(sol.validMountainArray(arr))
