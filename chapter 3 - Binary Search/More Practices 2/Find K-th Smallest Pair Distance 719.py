import random

from typing import List


class Solution:
	def smallestDistancePair(self, nums: List[int], k: int) -> int:
		nums.sort()

		low = 0
		high = nums[-1]
		while low < high:
			mid = low + (high - low) // 2

			count = self.helper_sliding_count(nums, mid)
			if count >= k:
				high = mid
			else:
				low = mid + 1

		return low

	def helper_sliding_count(self, nums: List[int], k: int) -> int:
		left = 0
		count = 0
		for right in range(len(nums)):
			while (nums[right] - nums[left]) > k:
				left += 1
			count += (right - left)

		return count


if __name__ == "__main__":
	sol = Solution()

	nums = [1, 3, 1]
	k = 1
	print(sol.smallestDistancePair(nums, k))
