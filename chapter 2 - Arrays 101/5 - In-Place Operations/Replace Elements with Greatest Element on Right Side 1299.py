from typing import List


class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		lastMax = arr[-1]
		for i in range(len(arr) - 2, -1, -1):
			k = arr[i]
			arr[i] = lastMax
			if k >= lastMax:
				lastMax = k

		arr[-1] = -1
		return arr

if __name__ == "__main__":
	sol = Solution()
	arr = [-4, -1, 0, 3, 10, 0]
	# arr = [17, 18, 5, 4, 6, 1]
	sol.replaceElements(arr)
	print(arr)
