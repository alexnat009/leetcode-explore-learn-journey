from collections import Counter


class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		return not Counter(ransomNote) - Counter(magazine)


if __name__ == "__main__":
	sol = Solution()
	print(sol.canConstruct(ransomNote="aa", magazine="aab"))
