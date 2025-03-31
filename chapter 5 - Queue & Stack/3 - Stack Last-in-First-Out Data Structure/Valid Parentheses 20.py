from collections import deque


class Solution:
	def isValid(self, s: str) -> bool:
		if not s or len(s) % 2 != 0 or s[0] not in ["{", "(", "["]:
			return False

		parentheses = {
			"{": "}",
			"(": ")",
			"[": "]"
		}
		stack = deque([])
		for i in s:
			if i in parentheses:
				stack.append(i)
			elif len(stack) == 0 or parentheses[stack.pop()] != i:
				return False
		return len(stack) == 0


if __name__ == "__main__":
	sol = Solution()
	s = "({})"
	print(sol.isValid(s))
