from typing import List


class Solution:
	def duplicateZeros(self, arr: List[int]) -> None:
		"""
		Do not return anything, modify arr in-place instead.
		"""
		zeros = arr.count(0)
		n = len(arr)

		for i in range(n - 1, -1, -1):
			if i + zeros < n:
				arr[i + zeros] = arr[i]

			if arr[i] == 0:
				zeros -= 1
				if i + zeros < n:
					arr[i + zeros] = 0


# print(tmp[:n + 1])


if __name__ == "__main__":
	sol = Solution()
	# arr = [-4, -1, 0, 3, 10, 0]
	arr = [1, 0, 2, 3, 0, 4, 5, 0]
	sol.duplicateZeros(arr)
	print(arr)
