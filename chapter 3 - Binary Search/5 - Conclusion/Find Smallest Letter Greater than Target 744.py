from typing import List


class Solution:
	def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		low = 0
		high = len(letters) - 1
		while low < high:
			mid = low + (high - low) // 2
			if letters[mid] <= target:
				low = mid + 1
			else:
				high = mid
		return letters[low] if letters[low] > target else letters[0]


if __name__ == "__main__":
	sol = Solution()

	letters = ["c", "f", "j"]
	target = "z"
	print(sol.nextGreatestLetter(letters, target))
