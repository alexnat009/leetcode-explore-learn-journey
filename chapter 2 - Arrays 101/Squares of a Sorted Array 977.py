from typing import List


class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		n = len(nums)
		res = [0] * n
		leftId, rightId = 0, n - 1
		for i in range(n - 1, -1, -1):
			if abs(nums[leftId]) >= abs(nums[rightId]):
				res[i] = nums[leftId] ** 2
				leftId += 1
			else:
				res[i] = nums[rightId] ** 2
				rightId -= 1
		return res


if __name__ == "__main__":
	sol = Solution()
	nums = [-4, -1, 0, 3, 10]
	print(sol.sortedSquares(nums))
