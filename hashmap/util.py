from hashlib import md5

def _assert_str(value):
	if type(value) is not str:
			raise TypeError(f'Invalid Type, expected str got: {type(value)}')

def _assert_int(value):
	if type(value) is not int:
			raise TypeError(f'Invalid Type, expected str got: {type(value)}')

def _hash_key(key, size):
	result = int(md5(key.encode('UTF-8')).hexdigest(), 16) % size
	return result

