from typing import List


class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		if len(nums) < 3:
			return max(nums)
		else:
			tmp = sorted(nums)
			k = set()
			for i in range(len(tmp) - 1, -1, -1):
				k.add(tmp[i])
				if len(k) == 3:
					return tmp[i]
			if len(k) < 3:
				return max(k)


if __name__ == "__main__":
	sol = Solution()
	heights = [1, 1, 1, 1, 14]
	print(sol.thirdMax(heights))
