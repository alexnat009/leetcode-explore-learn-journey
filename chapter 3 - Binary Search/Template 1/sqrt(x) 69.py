import math


class Solution:
	def mySqrt(self, x: int) -> int:
		if x == 0:
			return 0
		if x < 4:
			return 1
		low = 2
		high = x // 2
		while low <= high:
			mid = low + (high - low) // 2
			if mid ** 2 <= x < (mid + 1) ** 2:
				return mid
			if mid ** 2 < x:
				low = mid + 1
			elif mid ** 2 > x:
				high = mid - 1
		return low


if __name__ == "__main__":
	sol = Solution()
	x = 22
	print(sol.mySqrt(x))
