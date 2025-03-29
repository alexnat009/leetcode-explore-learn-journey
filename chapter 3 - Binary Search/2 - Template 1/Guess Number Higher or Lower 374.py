import random
import math


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:

	def __init__(self):
		self.__pick = None

	def __guess(self, num: int) -> int:
		if num > self.__pick:
			return -1  # num > pick → return -1
		elif num < self.__pick:
			return 1  # num < pick → return 1
		else:
			return 0  # num == pick → return 0

	def guessNumber(self, n: int) -> int:
		self.__pick = random.randint(0, n)
		low = 0
		high = n
		while low <= high:
			mid = low + (high - low) // 2
			if self.__guess(mid) == 0:
				print(f'You guessed right, my pick was {self.__pick}')
				return mid
			elif self.__guess(mid) == -1:
				high = mid - 1
			else:
				low = mid + 1
		return low


if __name__ == "__main__":
	sol = Solution()

	print(sol.guessNumber(100))

