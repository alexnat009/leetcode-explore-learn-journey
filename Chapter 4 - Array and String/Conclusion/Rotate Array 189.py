from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		k = k % n
		count = 0

		start = 0
		while count < n:
			current = start
			prev = nums[start]

			while True:
				next_id = (current + k) % n
				nums[next_id], prev = prev, nums[next_id]
				current = next_id
				count += 1

				if current == start:
					break
			start += 1
			if count >= n:
				break


if __name__ == "__main__":
	sol = Solution()
	# nums = [10, 2, 3]

	nums = [-1, -100, 3, 99]
	k = 2

	print(sol.rotate(nums, k))
	print(nums)
