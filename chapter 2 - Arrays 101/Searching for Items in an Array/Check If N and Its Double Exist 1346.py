from typing import List


class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		for i in range(len(arr)):
			for j in range(i + 1, len(arr)):
				if arr[i] == arr[j] * 2 or arr[j] == 2 * arr[i]:
					return True
		return False


if __name__ == "__main__":
	sol = Solution()
	arr = [-2, 0, 10, -19, 4, 6, -8]
	print(sol.checkIfExist(arr))
