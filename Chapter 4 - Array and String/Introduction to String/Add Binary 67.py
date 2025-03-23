class Solution:
	def addBinary(self, a: str, b: str) -> str:
		carry = 0
		res = []

		a = list(a)
		b = list(b)
		while a or b or carry:
			if a:
				carry += int(a.pop())
			if b:
				carry += int(b.pop())
			res.append(str(carry % 2))
			carry //= 2
		return "".join(res[::-1])


if __name__ == "__main__":
	sol = Solution()

	a = "1010"
	b = "1011"
	print(sol.addBinary(a, b))
