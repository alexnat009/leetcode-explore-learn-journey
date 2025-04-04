class MyQueue:

	def __init__(self):
		self.popStack = []
		self.pushStack = []

	def push(self, x: int) -> None:
		self.pushStack.append(x)

	def pop(self) -> int:
		if self.popStack:
			return self.popStack.pop()
		else:
			while self.pushStack:
				self.popStack.append(self.pushStack.pop())
			return self.pop()

	def peek(self) -> int:
		if self.popStack:
			return self.popStack[-1]
		else:
			while self.pushStack:
				self.popStack.append(self.pushStack.pop())
			return self.peek()

	def empty(self) -> bool:
		return False if self.popStack or self.pushStack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# Test case 1: Basic functionality
if __name__ == "__main__":
	queue = MyQueue()
	queue.push(1)
	queue.push(2)
	assert queue.peek() == 1, "Test case 1 failed"
	assert queue.pop() == 1, "Test case 1 failed"
	assert not queue.empty(), "Test case 1 failed"

	# Test case 2: Empty queue
	queue = MyQueue()
	assert queue.empty(), "Test case 2 failed"

	# Test case 3: Push and pop multiple elements
	queue = MyQueue()
	queue.push(1)
	queue.push(2)
	queue.push(3)
	assert queue.pop() == 1, "Test case 3 failed"
	assert queue.pop() == 2, "Test case 3 failed"
	assert queue.pop() == 3, "Test case 3 failed"
	assert queue.empty(), "Test case 3 failed"

	# Test case 4: Peek after multiple pushes
	queue = MyQueue()
	queue.push(10)
	queue.push(20)
	queue.push(30)
	assert queue.peek() == 10, "Test case 4 failed"
	assert queue.pop() == 10, "Test case 4 failed"
	assert queue.peek() == 20, "Test case 4 failed"
	assert queue.pop() == 20, "Test case 4 failed"
	assert queue.peek() == 30, "Test case 4 failed"
	assert queue.pop() == 30, "Test case 4 failed"
	assert queue.empty(), "Test case 4 failed"
