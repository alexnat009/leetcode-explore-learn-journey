class Solution:
	def myPow(self, x: float, n: int) -> float:
		def helper_pow(x, n):
			if x == 0:
				return 0
			if n == 0:
				return 1

			res = helper_pow(x, n // 2)
			res = res * res
			return x * res if n % 2 else res

		res = helper_pow(x, abs(n))

		return res if n > 0 else 1 / res


if __name__ == "__main__":
	sol = Solution()

	print(sol.myPow(2, -2))
