

class LinkedListNode:
	def __init__(self, data=None):
		self.data = data
		self.__child = None

	@property
	def length(self):
		return len(self)

	def next(self):
		return self.__child

	def connect(self, node):
		if self.__child is None:
			self.__child = node
		else:
			self.__child.connect(node)

	def __len__(self):
		length = 1
		node = self

		while node.next() != None:
			length += 1
			node = node.next()

		return length

