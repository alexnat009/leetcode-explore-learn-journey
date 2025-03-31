from collections import deque


class MinStack:

	def __init__(self):
		self.stack_min = deque([])
		self.stack = deque([])

	def push(self, val: int) -> None:
		if not self.stack and not self.stack_min:
			self.stack.append(val)
			self.stack_min.append(val)
		elif val <= self.stack_min[-1]:
			self.stack_min.append(val)
			self.stack.append(val)
		else:
			self.stack.append(val)

	def pop(self) -> None:
		if self.stack:
			if self.stack.pop() == self.stack_min[-1]:
				self.stack_min.pop()

	def top(self) -> int:
		if self.stack:
			return self.stack[-1]

	def getMin(self) -> int:
		if self.stack:
			return self.stack_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
	sol = MinStack()

	sol.push(-2)
	print(sol.stack)
	sol.push(0)
	print(sol.stack)
	sol.push(-3)
	print(sol.stack)
	print(sol.getMin())
	sol.pop()
	print(sol.stack)
	print(sol.top())
	print(sol.getMin())
