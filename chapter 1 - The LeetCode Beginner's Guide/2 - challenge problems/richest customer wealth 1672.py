from typing import List


class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		maxWealth = 0
		for i in accounts:
			tmp = sum(i)
			maxWealth = max(maxWealth, tmp)
		return maxWealth


if __name__ == "__main__":
	sol = Solution()
	accounts = [[1, 5], [7, 3], [3, 5]]
	print(sol.maximumWealth(accounts))
