class Solution:
	def addBinary(self, a: str, b: str) -> str:
		return str(bin(int(a, 2) + (int(b, 2))))[2:]


if __name__ == "__main__":
	sol = Solution()

	a = "1010"
	b = "1011"
	print(sol.addBinary(a, b))
