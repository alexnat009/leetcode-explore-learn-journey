from typing import List


class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		for token in tokens:
			if token not in {"+", "-", "*", "/"}:
				stack.append(int(token))
			else:
				x = stack.pop()
				y = stack.pop()
				if token == "/":
					stack.append(int(y / x))
				elif token == "-":
					stack.append(y - x)
				elif token == "+":
					stack.append(x + y)
				else:
					stack.append(x * y)
		return stack.pop()


if __name__ == "__main__":
	sol = Solution()
	tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
	print(sol.evalRPN(tokens))

