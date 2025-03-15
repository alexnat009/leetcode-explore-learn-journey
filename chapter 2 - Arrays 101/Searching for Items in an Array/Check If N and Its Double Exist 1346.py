from collections import Counter
from typing import List


class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		cnt = Counter()
		for i in arr:
			cnt[i] += 1

		for i in arr:
			if i != 0 and i * 2 in cnt:
				return True
			if i == 0 and cnt.get(i) > 1:
				return True
		return False


if __name__ == "__main__":
	sol = Solution()
	arr = [-2, 0, 10, -19, 4, 6, -8]

	print(sol.checkIfExist(arr))
