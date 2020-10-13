"""Test cases for Linked List
Author: Ben Paulson
"""

import unittest
from ordered_list import *

class Lab1Tests(unittest.TestCase):

    def setUp(self):
        self.node = Node(4, None, None)
        self.common_node = Node(4, None, None)
        self.node1 = Node(10, self.common_node, None)
        self.node2 = Node(10, self.common_node, None)
        #self.node1.next = self.node2
        self.empty_list = OrderedList()
        self.empty_list2 = OrderedList()


    def test_node_eq(self):
        self.assertEqual(self.common_node, self.common_node)
        self.assertEqual(self.node2, self.node1)
        self.assertEqual(self.node, self.common_node)
        self.assertNotEqual(self.node, self.node1)


    def test_node_repr(self):
        self.assertEqual(self.common_node.__repr__(), "Node(4, None)")
        self.assertEqual(self.node1.__repr__(), "Node(10, Node(4, None))")
        self.assertEqual(self.node2.__repr__(), "Node(10, Node(4, None))")


    def test_ordered_list_add(self):
        self.empty_list.add(1)
        # Check that string repr is the same since they are not the same type
        self.assertEqual(self.empty_list.__repr__(),
            Node(1, None, None).__repr__())
        self.empty_list.add(3)
        self.assertEqual(self.empty_list.__repr__(),
            "Node(1, Node(3, None))")
        self.empty_list2.add(2)
        self.empty_list2.add(1)
        self.assertEqual(self.empty_list2.__repr__(),
            "Node(1, Node(2, None))")
        self.empty_list.add(0)
        self.assertEqual(self.empty_list.__repr__(),
            "Node(0, Node(1, Node(3, None)))")
        self.empty_list2.add(3)
        self.assertEqual(self.empty_list2.__repr__(),
            "Node(1, Node(2, Node(3, None)))")
        self.empty_list.add(2)
        self.assertEqual(self.empty_list.__repr__(),
            "Node(0, Node(1, Node(2, Node(3, None))))")
        self.assertNotEqual(self.empty_list, self.empty_list2)
        self.empty_list2.add(0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(500)
        self.assertNotEqual(self.empty_list, self.empty_list2)


    def test_ordered_list_is_empty(self):
        self.assertTrue(self.empty_list.is_empty())
        self.empty_list.add(3)
        self.assertFalse(self.empty_list.is_empty())
        self.empty_list.add(5)
        self.assertFalse(self.empty_list.is_empty())


    def test_ordered_list_remove(self):
        self.empty_list.add(3)
        self.assertEqual(self.empty_list.remove(3), 0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(3)
        self.empty_list.add(2)
        self.empty_list2.add(3)
        self.empty_list2.add(2)
        self.empty_list.add(1)
        self.assertEqual(self.empty_list.remove(1), 0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(1)
        self.assertEqual(self.empty_list.remove(3), 2)
        self.assertEqual(self.empty_list.__repr__(),
            "Node(1, Node(2, None))")
        self.empty_list.add(3)
        self.assertEqual(self.empty_list.remove(2), 1)
        self.assertEqual(self.empty_list.__repr__(),
            "Node(1, Node(3, None))")
        self.empty_list.remove(1)
        self.empty_list.remove(3)
        self.assertRaises(ValueError, self.empty_list.remove, 3)
        self.empty_list.add(4)
        self.assertRaises(ValueError, self.empty_list.remove, 6)
        self.empty_list.add(4)
        self.empty_list.add(5)
        self.empty_list.add(6)
        self.empty_list.remove(5)


    def test_ordered_list_search_forward(self):
        for i in range(10):
            self.empty_list.add(i)
        self.assertTrue(self.empty_list.search_forward(3))
        self.assertTrue(self.empty_list.search_forward(0))
        self.assertTrue(self.empty_list.search_forward(9))
        self.assertFalse(self.empty_list.search_forward(10))


    def test_ordered_list_search_backward(self):
        for i in range(10):
            self.empty_list.add(i)
        self.assertTrue(self.empty_list.search_backward(3))
        self.assertTrue(self.empty_list.search_backward(0))
        self.assertTrue(self.empty_list.search_backward(9))
        self.assertFalse(self.empty_list.search_backward(10))


    def test_ordered_list_size(self):
        self.assertEqual(self.empty_list.size(), 0)
        self.empty_list.add(0)
        self.assertEqual(self.empty_list.size(), 1)
        for i in range(1, 10):
            self.empty_list.add(i)
        self.assertEqual(self.empty_list.size(), 10)


    def test_ordered_list_index(self):
        self.empty_list.add(0)
        self.assertEqual(self.empty_list.index(0), 0)
        for i in range(1, 10):
            self.empty_list.add(i)
        self.assertEqual(self.empty_list.index(9), 9)
        self.empty_list.add(15)
        self.assertEqual(self.empty_list.index(15), 10)
        self.assertRaises(ValueError, self.empty_list.index, 100)


    def test_ordered_list_pop(self):
        for i in range(10):
            self.empty_list.add(i * 2)
        self.assertEqual(self.empty_list.pop(), 18)
        for i in range(9):
            self.empty_list2.add(i * 2)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.assertEqual(self.empty_list.pop(2), 4)
        self.assertEqual(self.empty_list.pop(2), 6)
        self.assertEqual(self.empty_list.pop(6), 16)
        self.assertRaises(IndexError, self.empty_list.pop, 100)
        self.assertEqual(self.empty_list2.pop(0), 0)
        self.assertEqual(self.empty_list2.pop(self.empty_list2.size() - 1), 16)
        self.empty_list = OrderedList()
        self.assertRaises(IndexError, self.empty_list.pop)
        for i in range(5):
            self.empty_list.add(i)
        self.assertEqual(self.empty_list.pop(3), 3)



if __name__ == '__main__':
    unittest.main()
