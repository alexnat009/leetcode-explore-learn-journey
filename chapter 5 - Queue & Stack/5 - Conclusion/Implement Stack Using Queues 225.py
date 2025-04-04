from collections import deque


class MyStack:

	def __init__(self):
		self.pushQueue = deque()
		self.popQueue = deque()

	def push(self, x: int) -> None:
		self.pushQueue.append(x)

	def pop(self) -> int:
		while len(self.pushQueue) > 1:
			self.popQueue.append(self.pushQueue.popleft())
		res = self.pushQueue.popleft()
		self.pushQueue, self.popQueue = self.popQueue, self.pushQueue
		return res

	def top(self) -> int:
		while len(self.pushQueue) > 1:
			self.popQueue.append(self.pushQueue.popleft())
		res = self.pushQueue.popleft()
		self.popQueue.append(res)
		self.pushQueue, self.popQueue = self.popQueue, self.pushQueue
		return res

	def empty(self) -> bool:
		return not self.pushQueue


if __name__ == "__main__":
	stack = MyStack()

	# Test case 1: Push elements and check top
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	assert stack.top() == 4, f"Expected top to be 4, but got {stack.top()}"

	# Test case 2: Pop element and check top
	stack.pop()
	assert stack.top() == 3, f"Expected top to be 3, but got {stack.top()}"

	# Test case 3: Pop element and check top
	stack.pop()
	assert stack.top() == 2, f"Expected top to be 2, but got {stack.top()}"

	# Test case 4: Check if stack is empty
	assert not stack.empty(), "Expected stack to be not empty"

	# Test case 5: Pop all elements and check if stack is empty
	stack.pop()
	stack.pop()
	assert stack.empty(), "Expected stack to be empty"
