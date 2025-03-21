from typing import List


class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		for i in range(len(digits) - 1, -1, -1):
			if digits[i] < 9:
				digits[i] += 1
				return digits
			digits[i] = 0

		return [1] + [0] * len(digits)


if __name__ == "__main__":
	sol = Solution()

	nums = [1]
	for i in range(100):
		nums = sol.plusOne(nums)
		print(nums)
