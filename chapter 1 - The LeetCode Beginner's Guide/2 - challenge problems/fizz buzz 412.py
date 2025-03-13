from typing import List


class Solution:
	def fizzBuzz(self, n: int) -> List[str]:
		tmp = []
		for i in range(1, n + 1):
			tmp.append(
				"FizzBuzz" if i % 15 == 0 else
				"Buzz" if i % 5 == 0 else
				"Fizz" if i % 3 == 0 else
				str(i)
			)
		return tmp


if __name__ == "__main__":
	sol = Solution()

	print(sol.fizzBuzz(7))
