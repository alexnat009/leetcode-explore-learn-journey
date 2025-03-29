class MyCircularQueue:

	def __init__(self, k: int):
		self.queue = [-1] * k
		self.head = None
		self.tail = None

	def enQueue(self, value: int) -> bool:
		if self.isEmpty():
			self.head = 0
			self.tail = 0
			self.queue[self.head] = value
			return True
		else:
			if self.isFull():
				return False
			if self.tail + 1 < len(self.queue):
				self.tail += 1
			else:
				self.tail = 0

			self.queue[self.tail] = value
			return True

	def deQueue(self) -> bool:
		if self.isEmpty():
			return False

		self.queue[self.head] = -1
		if self.isEmpty():
			self.head = self.tail = 0
			return True
		if self.head + 1 < len(self.queue):
			self.head += 1
		else:
			self.head = 0

		return True

	def Front(self) -> int:
		if self.isEmpty():
			return -1
		return self.queue[self.head]

	def Rear(self) -> int:
		if self.isEmpty():
			return -1
		return self.queue[self.tail]

	def isEmpty(self) -> bool:
		return all(x == -1 for x in self.queue)

	def isFull(self) -> bool:
		return all(x != -1 for x in self.queue)


if __name__ == "__main__":
	sol = MyCircularQueue(5)

	print(sol.queue)
	print(sol.isEmpty())
	print(sol.enQueue(5))
	print(sol.queue)
