class Solution:
	def numberOfSteps(self, num: int) -> int:
		# My Solution
		def helper(n, num):
			if num == 0:
				return n
			if num % 2 == 0:
				return helper(n + 1, num / 2)
			else:
				return helper(n + 1, num - 1)

		return helper(0, num)

