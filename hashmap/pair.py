from hashmap import *
from hashmap.util import _assert_str, _assert_int

class KeyValuePair:
	def __init__(self, key:str, hashed_key, value):
		_assert_str(key)
		_assert_int(hashed_key)

		self.__key = key
		self.__hashed_key = hashed_key
		self.__value = value

	# Properties
	@property
	def key(self):
		return self.__key

	@property
	def hashed_key(self):
		return self.__hashed_key

	@property
	def value(self):
		return self.__value

