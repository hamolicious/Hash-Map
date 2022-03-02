import unittest
from os import system
import string
from random import choice, randint

import sys
sys.path.insert(1, 'F:\\Programing_Projects\\Python\\---FromScratch---\\hashmap')
from hashmap import Hash
from hashmap.util import _hash_key

class TestHashingCollisions(unittest.TestCase):
	__NUM_OF_TESTS = 1000000
	__ACCEPTABLE_CHANCE_OF_COLLISION = 1#%

	def test_collision(self):
		max_collisions = TestHashingCollisions.__NUM_OF_TESTS * (TestHashingCollisions.__ACCEPTABLE_CHANCE_OF_COLLISION / 100)

		random_string = lambda size : ''.join([choice(string.ascii_letters) for _ in range(size)])

		# generate __NUM_OF_TESTS unique keys
		test_keys = set()
		while len(test_keys) < TestHashingCollisions.__NUM_OF_TESTS:
			test_keys.add(random_string(randint(1, 64))) # key to hash

		# test above generated keys
		generated_indecies = {}
		my_hash = Hash()
		for key in test_keys:
			index = _hash_key(key, my_hash._Hash__size)

		num_of_collisions = 0
		for item in my_hash._Hash__buckets:
			if item is None : continue
			num_of_collisions += len(item)-1 # len of linked list (-1 to not count original)

		print(f'Number of Collisions after {TestHashingCollisions.__NUM_OF_TESTS:,} tests: {num_of_collisions:,} ({(num_of_collisions / TestHashingCollisions.__NUM_OF_TESTS) * 100:02}%)')
		self.assertLess(num_of_collisions, max_collisions)


class TestHashMethods(unittest.TestCase):
	def test_insert(self):
		hash = Hash()
		hash['key'] = "Hello World"
		self.assertEqual(hash.get('key'), 'Hello World')

	def test_multiple_insert(self):
		hash = Hash()
		test_dict = {}
		items = ['key', 'foo', 'bar', 'hello world', 'hello_world', 'hello World', 'bar']

		for item in items:
			i = randint(0, 1000)
			hash[item] = i
			test_dict[item] = i

		for item in items:
			self.assertEqual(hash[item], test_dict[item])

	def test_wrong_type(self):
		hash = Hash()
		with self.assertRaises(TypeError) : hash[3]
		with self.assertRaises(TypeError) : hash[0.2]
		with self.assertRaises(TypeError) : hash[0x02]

	def test_non_existent_key(self):
		hash = Hash()
		with self.assertRaises(KeyError) : hash["key"]
		with self.assertRaises(KeyError) : hash["foo"]
		with self.assertRaises(KeyError) : hash["bar"]

	def test_default_return(self):
		hash = Hash()
		hash['foo'] = 12/5
		self.assertEqual(hash.get('none', 5), 5)
		self.assertEqual(hash.get('random_key', True), True)
		self.assertEqual(hash.get('foo', False), 12/5)
		self.assertEqual(hash.get('none', 'blue'), 'blue')

	def test_len(self):
		hash = Hash()
		items = ['key', 'foo', 'bar', 'hello world', 'hello_world', 'hello World', 'bar']

		for item in items:
			i = randint(0, 1000)
			hash[item] = i

		self.assertEqual(len(hash), len(set(items)))

	def test_resize(self):
		hash = Hash()

		starting_size = hash._Hash__size
		fill_to_resize = int(starting_size * Hash._Hash__MAX_LOAD_FACTOR) + 1 # for good measure
		expected_new_size = starting_size * (1 + Hash._Hash__RESIZE_FACTOR)

		hash['perm_key'] = 'very important value, plz dont delete'

		for i in range(fill_to_resize):
			hash[str(i)] = randint(0, 1000)

		self.assertEqual(hash.get('perm_key'), 'very important value, plz dont delete', 'Overwrote values')
		self.assertEqual(expected_new_size, hash._Hash__size, 'Not the correct size')

def suite():
	suite = unittest.TestSuite()
	# suite.addTest(TestHashingCollisions('test_collision'))
	suite.addTest(TestHashMethods('test_insert'))
	suite.addTest(TestHashMethods('test_multiple_insert'))
	suite.addTest(TestHashMethods('test_default_return'))
	suite.addTest(TestHashMethods('test_wrong_type'))
	suite.addTest(TestHashMethods('test_non_existent_key'))
	suite.addTest(TestHashMethods('test_resize'))
	suite.addTest(TestHashMethods('test_len'))
	return suite

if __name__ == '__main__':
	system('cls')
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())