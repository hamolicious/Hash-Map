import unittest
from os import system
import string
from random import choice, randint

import sys
sys.path.insert(1, 'F:\\Programing_Projects\\Python\\---FromScratch---\\hash')
from hashmap import LinkedListNode


class TestLinkedListMethods(unittest.TestCase):
	def create_list(self):
		l = LinkedListNode()
		self.assertEqual(type(l), LinkedListNode)

	def link_list(self):
		l1 = LinkedListNode('1')
		l2 = LinkedListNode('2')
		l1.connect(l2)

		self.assertEqual(l1.next().data, '2')

	def propagate_list(self):
		l1 = LinkedListNode('1')
		l2 = LinkedListNode('2')
		l3 = LinkedListNode('3')
		l4 = LinkedListNode('4')
		l1.connect(l2)
		l1.connect(l3)
		l1.connect(l4)

		self.assertEqual(l1.next().next().next().data, '4')
		self.assertEqual(l1.next().next().next().next(), None)

	def test_length(self):
		l1 = LinkedListNode('1')
		l2 = LinkedListNode('2')
		l3 = LinkedListNode('3')
		l4 = LinkedListNode('4')
		l1.connect(l2)
		l1.connect(l3)
		l1.connect(l4)

		self.assertEqual(l1.length, 4)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(TestLinkedListMethods('create_list'))
	suite.addTest(TestLinkedListMethods('link_list'))
	suite.addTest(TestLinkedListMethods('propagate_list'))
	suite.addTest(TestLinkedListMethods('test_length'))
	return suite

if __name__ == '__main__':
	system('cls')
	system('color')
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())