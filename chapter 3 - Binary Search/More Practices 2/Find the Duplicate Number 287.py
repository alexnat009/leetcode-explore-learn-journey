from typing import List


class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		slowP = fastP = 0
		while True:
			slowP = nums[slowP]
			fastP = nums[nums[fastP]]
			if slowP == fastP:
				break
		slowP2 = 0
		while True:
			slowP = nums[slowP]
			slowP2 = nums[slowP2]
			if slowP == slowP2:
				return slowP


if __name__ == "__main__":
	sol = Solution()

	numbers = [1, 2, 3, 2]

	print(sol.findDuplicate(numbers))
