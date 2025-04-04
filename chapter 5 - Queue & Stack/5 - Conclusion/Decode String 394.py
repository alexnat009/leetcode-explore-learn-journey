from collections import deque


class Solution:
	def decodeString(self, s: str) -> str:

		open_bracket = '['
		close_bracket = ']'
		repeatStack = deque()
		symbolsStack = deque()
		current_string = []
		number = 0

		for i in s:
			if i.isdigit():
				number = number * 10 + int(i)
			elif i == open_bracket:
				repeatStack.append(number)
				symbolsStack.append(current_string)
				current_string = []
				number = 0
			elif i == close_bracket:
				repeat_count = repeatStack.pop()
				previous_string = symbolsStack.pop()
				current_string = previous_string + current_string * repeat_count
			else:
				current_string.append(i)
		return "".join(current_string)


if __name__ == "__main__":
	sol = Solution()
	s = "3[ab2[a]3[c2[b]]]"
	print(sol.decodeString(s))
