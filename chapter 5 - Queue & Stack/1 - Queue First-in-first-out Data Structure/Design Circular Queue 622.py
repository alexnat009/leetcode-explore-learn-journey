class MyCircularQueue:

	def __init__(self, k: int):
		self.queue = []
		self.k = k

	def enQueue(self, value: int) -> bool:
		if self.k > 0:
			self.queue.append(value)
			self.k -= 1
			return True
		return False

	def deQueue(self) -> bool:
		if self.queue:
			self.queue.pop(0)
			self.k += 1
			return True
		return False

	def Front(self) -> int:
		if self.queue:
			return self.queue[0]
		return -1

	def Rear(self) -> int:
		if self.queue:
			return self.queue[-1]
		return -1

	def isEmpty(self) -> bool:
		if not self.queue:
			return True
		return False

	def isFull(self) -> bool:
		if self.k == 0:
			return True
		return False


if __name__ == "__main__":
	sol = MyCircularQueue(5)

	print(sol.queue)
	print(sol.isEmpty())
	print(sol.enQueue(5))
	print(sol.queue)
