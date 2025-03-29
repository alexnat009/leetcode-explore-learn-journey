class Solution:
	def reverseWords(self, s: str) -> str:
		return " ".join([word[::-1] for word in s.split()])


if __name__ == "__main__":
	sol = Solution()

	s = "Let's take LeetCode contest"

	print(sol.reverseWords(s))
