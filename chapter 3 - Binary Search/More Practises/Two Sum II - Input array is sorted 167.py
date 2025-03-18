from typing import List


class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		leftP, rightP = 0, len(numbers) - 1

		while leftP < rightP:
			numSum = numbers[leftP] + numbers[rightP]
			if numSum == target:
				return [leftP + 1, rightP + 1]
			elif numSum < target:
				leftP += 1
			else:
				rightP -= 1
		return [-1, -1]


if __name__ == "__main__":
	sol = Solution()

	numbers = [1, 2, 7, 11, 15, 20]
	target = 17

	print(sol.twoSum(numbers, target))
