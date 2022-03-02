from hashmap import *
from hashmap.util import _hash_key, _assert_str


class Hash:
	__DEFAULT_SIZE = 200
	__MAX_LOAD_FACTOR = 0.6
	__RESIZE_FACTOR = 0.5

	def __init__(self):
		self.__buckets = [None for _ in range(Hash.__DEFAULT_SIZE)]

	# Properties
	@property
	def __size(self):
		return len(self.__buckets)

	@property
	def __load_factor(self):
		return self.__entries_occupied / self.__size

	@property
	def __entries_occupied(self):
		length = 0
		for entry in self.__buckets:
			if entry is None : continue
			length += len(entry)
		return length

	# Privates
	def __fetch(self, key):
		"""Gets the node that contains the data for the key

		Returns:
			LinkedListNode: linked list node containing the data for the requested key
		"""
		_assert_str(key)
		node = self.__buckets[_hash_key(key, self.__size)]
		if node is None : raise(KeyError(f'Key "{key}" does not exist'))
		if node.data.key == key : return node
		while True:
			if node is None : raise(KeyError(f'Key "{key}" does not exist'))
			if node.data.key == key : return node
			node = node.next()

	def __insert(self, key, value):
		_assert_str(key)
		pair = KeyValuePair(key, _hash_key(key, self.__size), value)
		node = self.__buckets[_hash_key(key, self.__size)]
		new_node = LinkedListNode(pair)

		if node is None : self.__buckets[_hash_key(key, self.__size)] = new_node       # create new node if it doesn't exist
		node = self.get(key)                                                           # otherwise, search for the key
		if node is None : self.__buckets[_hash_key(key, self.__size)].connect(new_node)
		else            : self.__buckets[_hash_key(key, self.__size)].data = pair

		if self.__load_factor >= Hash.__MAX_LOAD_FACTOR:
			self.__resize()

	def __delete(self, key):
		del self.__buckets[key]

	def __resize(self):
		# store key-value pairs
		pairs = []
		for item in self.__buckets:
			if item is None : continue
			# unpack lists
			while item is not None:
				pairs.append(item.data)
				item = item.next()

		# resize
		self.__buckets = [None for _ in range(int(self.__size + (self.__size * self.__RESIZE_FACTOR)))]

		# rehash
		for pair in pairs : self.__insert(pair.key, pair.value)

	# Public
	def get(self, key:str, default=None):
		"""Same as self['key'] but upon not finding the key, a `default` value is used

		Args:
			key (str): key to look for
			default (Any, optional): what to return if key not found. Defaults to None.

		Returns:
			Any|default: if key is found, returns data associated with the key, otherwise, returns the value in `default`
		"""
		try:
			val = self.__fetch(key).data.value
		except KeyError:
			return default
		return val

	# Overloads
	def __getitem__(self, key:str):
		return self.__fetch(key).data.value

	def __setitem__(self, key:str, value):
		self.__insert(key, value)

	def __delitem__(self, key):
		self.__delete(key)

	def __len__(self):
		return self.__entries_occupied

