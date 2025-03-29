from typing import List


class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		i = 0
		k = len(s) - 1
		while i <= k:
			s[i], s[k] = s[k], s[i]
			i += 1
			k -= 1


if __name__ == "__main__":
	sol = Solution()
	strs = list("hello")
	sol.reverseString(strs)
	print(strs)
