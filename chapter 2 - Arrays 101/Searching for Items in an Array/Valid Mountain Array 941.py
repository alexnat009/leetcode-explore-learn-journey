from typing import List


class Solution:
	def validMountainArray(self, arr: List[int]) -> bool:
		if len(arr) < 3:
			return False
		increase = arr[0]
		startDec = False
		startInc = False
		for i in range(1, len(arr)):
			if arr[i] == arr[i - 1]:
				return False
			if arr[i] >= increase:
				startInc = True
				if startDec:
					return False
				increase = arr[i]
			elif arr[i] < increase:
				increase = arr[i]
				startDec = True

		return True and startDec and startInc


if __name__ == "__main__":
	sol = Solution()
	# arr = [0, 2, 3, 4, 5]
	# arr = [2, 0, 2]
	# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	arr = [1, 7, 9, 5, 4, 1, 2]
	print(sol.validMountainArray(arr))
