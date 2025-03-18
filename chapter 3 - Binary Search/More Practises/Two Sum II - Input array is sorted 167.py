from typing import List


class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		leftP, rightP = 0, len(numbers) - 1
		res = [-1, -1]
		while leftP < rightP:
			if numbers[leftP] + numbers[rightP] == target:
				res = [leftP + 1, rightP + 1]
				break
			elif numbers[leftP] + numbers[rightP] < target:
				leftP += 1
			else:
				rightP -= 1
		return res


if __name__ == "__main__":
	sol = Solution()

	numbers = [2, 7, 11, 15]
	target = 9

	print(sol.twoSum(numbers, target))
