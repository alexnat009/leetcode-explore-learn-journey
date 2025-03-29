from collections import deque


class MyCircularQueue:

	def __init__(self, k: int):
		self.queue = deque([])
		self.size = k

	def enQueue(self, value: int) -> bool:
		if len(self.queue) == self.size:
			return False
		self.queue.append(value)
		return True

	def deQueue(self) -> bool:
		if not self.queue:
			return False
		self.queue.popleft()
		return True

	def Front(self) -> int:
		return self.queue[0] if self.queue else -1

	def Rear(self) -> int:
		return self.queue[-1] if self.queue else -1

	def isEmpty(self) -> bool:
		return not self.queue

	def isFull(self) -> bool:
		return len(self.queue) == self.size


if __name__ == "__main__":
	sol = MyCircularQueue(5)

	print(sol.queue)
	print(sol.isEmpty())
	print(sol.enQueue(5))
	print(sol.queue)
