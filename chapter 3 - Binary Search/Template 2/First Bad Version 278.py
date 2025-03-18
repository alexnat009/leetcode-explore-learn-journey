# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def __init__(self, bad):
		self.__badVersion = bad

	def isBadVersion(self, version: int) -> bool:
		return version >= self.__badVersion

	def firstBadVersion(self, n: int) -> int:
		low = 0
		high = n
		while low < high:
			mid = low + (high - low) // 2
			if self.isBadVersion(mid):
				high = mid
			else:
				low = mid + 1
		return low


if __name__ == "__main__":
	sol = Solution(4)
	n = 6
	print(sol.firstBadVersion(n))
