class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if not needle:
			return 0

		lps = self.longestPrefixSuffix(needle)
		i, k = 0, 0
		n, m = len(haystack), len(needle)

		while i < n:
			if haystack[i] == needle[k]:
				i += 1
				k += 1
				if k == m:
					return i - k
			else:
				if k > 0:
					k = lps[k - 1]
				else:
					i += 1

		return -1

	def longestPrefixSuffix(self, pattern: str):
		m = len(pattern)
		lps = [0] * m
		k = 0
		i = 1

		while i < m:
			if pattern[i] == pattern[k]:
				k += 1
				lps[i] = k
				i += 1
			elif k > 0:
				k = lps[k - 1]
			else:
				i += 1

		return lps


if __name__ == "__main__":
	sol = Solution()

	haystack = "mississippi"
	needle = "ssis"
	print(sol.strStr(haystack, needle))
