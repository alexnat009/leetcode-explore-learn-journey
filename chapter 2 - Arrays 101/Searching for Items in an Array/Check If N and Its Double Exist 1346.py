from typing import List


class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		tmpSet = set()
		for i in arr:
			if i not in tmpSet:
				tmpSet.add(i)
			elif i == 0 and i in tmpSet:
				return True

			if ((i * 2 in tmpSet) or (i / 2 in tmpSet)) and i != 0:
				return True
		return False




if __name__ == "__main__":
	sol = Solution()
	arr = [-2, 0, 10, -19, 4, 6, -8]

	print(sol.checkIfExist(arr))
