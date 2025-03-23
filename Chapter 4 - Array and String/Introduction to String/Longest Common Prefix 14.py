from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		prefix = []
		for i in zip(*strs):
			if len(set(i)) == 1:
				prefix.append(i[0])
			else:
				break
		return "".join(prefix)


if __name__ == "__main__":
	sol = Solution()
	strs = ["flower", "flow", "flight", "flowa"]
	print(sol.longestCommonPrefix(strs))
