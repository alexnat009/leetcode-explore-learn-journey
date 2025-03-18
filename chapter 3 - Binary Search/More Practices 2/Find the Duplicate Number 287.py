from typing import List


class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		setNums = set()
		for i in nums:
			if i in setNums:
				return i
			else:
				setNums.add(i)


if __name__ == "__main__":
	sol = Solution()

	numbers = [1, 3, 4, 2, 2]

	print(sol.findDuplicate(numbers))
