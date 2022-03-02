import unittest
from os import system
import string
from random import choice, randint

import sys
sys.path.insert(1, 'F:\\Programing_Projects\\Python\\---FromScratch---\\hashmap')
from hashmap import KeyValuePair


class TestKeyValuePair(unittest.TestCase):
	def test_create_pair(self):
		pair = KeyValuePair('key', 4, 'value')
		self.assertEqual(pair.key, 'key')
		self.assertEqual(pair.hashed_key, 4)
		self.assertEqual(pair.value, 'value')

	def test_invalid_key(self):
		self.assertRaises(TypeError, KeyValuePair, args=(123, 4, 'value'))

	def test_invalid_hash(self):
		self.assertRaises(TypeError, KeyValuePair, args=('key', 'wrong type', 'value'))


def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestKeyValuePair('test_create_pair'))
	suite.addTest(TestKeyValuePair('test_invalid_key'))
	suite.addTest(TestKeyValuePair('test_invalid_hash'))
	return suite

if __name__ == '__main__':
	system('cls')
	system('color')
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())