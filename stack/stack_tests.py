"""Stack tests.
Author: Ben Paulson
"""

import unittest
from stack_array import StackArray
from stack_linked import StackLinked
from node import Node


class Lab3Tests(unittest.TestCase):

    def setUp(self):
        self.empty_stack_array = StackArray()
        self.stack_array_1 = StackArray()
        self.stack_array_2 = StackArray()
        self.stack_array_2.push(3)
        self.stack_linked_1 = StackLinked()
        self.stack_linked_2 = StackLinked()


    def test_stack_array_eq(self):
        self.assertEqual(self.empty_stack_array, self.stack_array_1)
        self.stack_array_1.push(1)
        self.empty_stack_array.push(1)
        self.assertEqual(self.empty_stack_array, self.stack_array_1)
        self.stack_array_1.push(2)
        self.empty_stack_array.push(3)
        self.assertNotEqual(self.empty_stack_array, self.stack_array_1)


    def test_stack_array_repr(self):
        self.assertEqual(repr(self.empty_stack_array),
                         'StackArray([None, None])')
        self.assertEqual(repr(self.stack_array_2), 'StackArray([3, None])')
        self.stack_array_2.push(4)
        self.assertEqual(repr(self.stack_array_2),
                         'StackArray([3, 4, None, None])')


    def test_stack_array_push(self):
        self.stack_array_1.push(1)
        self.assertEqual(self.stack_array_1.arr, [1, None])
        self.stack_array_1.push(1)
        # This tests enlarge as well
        self.assertEqual(self.stack_array_1.arr, [1, 1, None, None])
        self.stack_array_1.push(2)
        self.assertEqual(self.stack_array_1.arr, [1, 1, 2, None])


    def test_stack_array_pop(self):
        self.assertRaises(IndexError, self.empty_stack_array.pop)
        self.stack_array_1.push(1)
        self.stack_array_1.push(1)
        self.stack_array_1.push(2)
        self.assertEqual(self.stack_array_1.arr, [1, 1, 2, None])
        self.assertEqual(self.stack_array_1.pop(), 2)
        self.assertEqual(self.stack_array_1.arr, [1, 1, None, None])
        self.assertEqual(self.stack_array_1.pop(), 1)
        self.assertEqual(self.stack_array_1.arr, [1, None])


    def test_stack_array_peek(self):
        self.stack_array_1.push(1)
        self.assertEqual(self.stack_array_1.peek(), 1)
        self.stack_array_1.push(2)
        self.assertEqual(self.stack_array_1.peek(), 2)
        self.stack_array_1.pop()
        self.assertEqual(self.stack_array_1.peek(), 1)


    def test_stack_array_peek_size_is_empty(self):
        self.assertRaises(IndexError, self.stack_array_1.peek)
        self.assertTrue(self.stack_array_1.is_empty())
        self.assertEqual(self.stack_array_1.size(), 0)
        self.stack_array_1.push(1)
        self.assertEqual(self.stack_array_1.peek(), 1)
        self.assertEqual(self.stack_array_1.size(), 1)
        self.stack_array_1.push(2)
        self.assertEqual(self.stack_array_1.peek(), 2)
        self.assertEqual(self.stack_array_1.size(), 2)
        self.stack_array_1.pop()
        self.assertEqual(self.stack_array_1.peek(), 1)
        self.assertEqual(self.stack_array_1.size(), 1)
        self.assertFalse(self.stack_array_1.is_empty())


    def test_stack_linked_eq(self):
        self.assertEqual(self.stack_linked_1, self.stack_linked_2)
        self.stack_linked_1.push(1)
        self.assertNotEqual(self.stack_linked_1, self.stack_linked_2)
        self.stack_linked_2.push(2)
        self.assertNotEqual(self.stack_linked_1, self.stack_linked_2)


    def test_stack_linked_repr(self):
        self.assertEqual(repr(self.stack_linked_1), 'StackLinked(None)')
        self.stack_linked_1.push(1)
        self.assertEqual(repr(self.stack_linked_1),
                         'StackLinked(Node(1, None))')
        self.stack_linked_1.push(2)
        self.assertEqual(repr(self.stack_linked_1),
                         'StackLinked(Node(2, Node(1, None)))')


    def test_stack_linked_push(self):
        self.assertEqual(self.stack_linked_1.top, None)
        self.stack_linked_1.push(1)
        self.assertEqual(self.stack_linked_1.top, Node(1, None))
        self.stack_linked_1.push(5)
        self.assertEqual(self.stack_linked_1.top, Node(5, Node(1, None)))


    def test_stack_linked_pop(self):
        self.stack_linked_1.push(5)
        self.stack_linked_1.push(1)
        self.stack_linked_1.push(3)
        self.assertEqual(self.stack_linked_1.top,
                         Node(3, Node(1, Node(5, None))))
        self.assertEqual(self.stack_linked_1.pop(), 3)
        self.assertEqual(self.stack_linked_1.top,
                         Node(1, Node(5, None)))
        self.assertEqual(self.stack_linked_1.pop(), 1)
        self.assertEqual(self.stack_linked_1.top,
                         Node(5, None))
        self.assertEqual(self.stack_linked_1.pop(), 5)
        self.assertEqual(self.stack_linked_1.top, None)
        self.assertRaises(IndexError, self.stack_linked_1.pop)


    def test_stack_linked_peek(self):
        self.assertRaises(IndexError, self.stack_linked_1.peek)
        self.stack_linked_1.push(5)
        self.assertEqual(self.stack_linked_1.peek(), 5)
        self.stack_linked_1.push(1)
        self.assertEqual(self.stack_linked_1.peek(), 1)
        self.stack_linked_1.push(3)
        self.assertEqual(self.stack_linked_1.peek(), 3)
        self.stack_linked_1.pop()
        self.assertEqual(self.stack_linked_1.peek(), 1)
        self.stack_linked_1.pop()
        self.assertEqual(self.stack_linked_1.peek(), 5)
        self.stack_linked_1.pop()
        self.assertRaises(IndexError, self.stack_linked_1.peek)


    def test_stack_linked_peek_size_is_empty(self):
        self.assertRaises(IndexError, self.stack_linked_1.peek)
        self.assertTrue(self.stack_linked_1.is_empty())
        self.assertEqual(self.stack_linked_1.size(), 0)
        self.stack_linked_1.push(1)
        self.assertEqual(self.stack_linked_1.peek(), 1)
        self.assertEqual(self.stack_linked_1.size(), 1)
        self.stack_linked_1.push(2)
        self.assertEqual(self.stack_linked_1.peek(), 2)
        self.assertEqual(self.stack_linked_1.size(), 2)
        self.stack_linked_1.pop()
        self.assertEqual(self.stack_linked_1.peek(), 1)
        self.assertEqual(self.stack_linked_1.size(), 1)
        self.assertFalse(self.stack_linked_1.is_empty())


if __name__ == '__main__':
    unittest.main()
