import math


class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		low = 0
		high = num
		while low <= high:
			mid = low + (high - low) // 2
			square = mid * mid
			if square == num:
				return True
			if square < num:
				low = mid + 1
			else:
				high = mid - 1
		return False


if __name__ == "__main__":
	sol = Solution()
	n = 4
	print(sol.isPerfectSquare(n))
	for i in range(0, 50):
		print(f'i={i}, {math.sqrt(i)}, {sol.isPerfectSquare(i)}') if sol.isPerfectSquare(i) else ""
