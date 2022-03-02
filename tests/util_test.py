import unittest
from os import system

import sys
sys.path.insert(1, 'F:\\Programing_Projects\\Python\\---FromScratch---\\hashmap')
from hashmap.util import _hash_key, _assert_str


class TestUtilMethods(unittest.TestCase):
	def test_assert_str_int(self) : self.assertRaises(TypeError, _assert_str, args=(5,))
	def test_assert_str_float(self) : self.assertRaises(TypeError, _assert_str, args=(float,))
	def test_assert_str_str(self) : self.assertEqual(None, _assert_str('hehehe'))


def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestUtilMethods('test_assert_str_int'))
	suite.addTest(TestUtilMethods('test_assert_str_float'))
	suite.addTest(TestUtilMethods('test_assert_str_str'))
	return suite

if __name__ == '__main__':
	system('cls')
	system('color')
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())