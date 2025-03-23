from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs:
			return ""

		min_str = min(strs, key=len)
		for i, char in enumerate(min_str):
			for s in strs:
				if s[i] != char:
					return min_str[:i]

		return min_str


if __name__ == "__main__":
	sol = Solution()
	strs = ["flower", "flow", "flight", "flowa"]
	print(sol.longestCommonPrefix(strs))
