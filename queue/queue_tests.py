"""Queue Tests
Author: Ben Paulson
"""

import unittest
from queue_linked import QueueLinked
from queue_array import QueueArray


class Lab4Tests(unittest.TestCase):

    def setUp(self):
        self.queue_linked_1 = QueueLinked()
        self.queue_linked_2 = QueueLinked()
        self.queue_linked_3 = QueueLinked(5)
        self.queue_array_1 = QueueArray()
        self.queue_array_2 = QueueArray()
        self.queue_array_3 = QueueArray(5)


    def test_queue_linked_eq(self):
        self.assertNotEqual(self.queue_linked_1, self.queue_linked_3)
        self.assertEqual(self.queue_linked_1, self.queue_linked_2)
        self.queue_linked_2.enqueue(2)
        self.assertNotEqual(self.queue_linked_1, self.queue_linked_2)
        self.queue_linked_1.enqueue(2)
        self.assertEqual(self.queue_linked_1, self.queue_linked_2)


    def test_queue_linked_repr(self):
        self.assertEqual(repr(self.queue_linked_3), "QueueLinked(None) Cap 5")
        self.assertEqual(repr(self.queue_linked_1), "QueueLinked(None) Cap 2")
        self.queue_linked_1.enqueue(2)
        self.assertEqual(repr(self.queue_linked_1),
                         "QueueLinked(Node(2, None)) Cap 2")
        self.queue_linked_1.enqueue(2)
        self.assertEqual(repr(self.queue_linked_1),
                         "QueueLinked(Node(2, Node(2, None))) Cap 2")


    def test_queue_linked_enqueue(self):
        self.queue_linked_1.enqueue(1)
        self.queue_linked_2.enqueue(1)
        self.assertEqual(self.queue_linked_1, self.queue_linked_2)
        self.assertEqual(self.queue_linked_1.size(), 1)
        self.queue_linked_1.enqueue(1)
        self.queue_linked_2.enqueue(2)
        self.assertNotEqual(self.queue_linked_1, self.queue_linked_2)
        self.assertEqual(self.queue_linked_1.size(), 2)
        self.assertEqual(self.queue_linked_2.rear.val, 2)
        self.assertRaises(IndexError, self.queue_linked_2.enqueue, 5)


    def test_queue_linked_dequeue(self):
        self.queue_linked_1.enqueue(1)
        self.queue_linked_2.enqueue(1)
        self.queue_linked_1.enqueue(1)
        self.queue_linked_2.enqueue(2)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(2)
        self.assertEqual(self.queue_linked_3.dequeue(), 1)
        self.assertEqual(self.queue_linked_3.dequeue(), 1)
        self.assertEqual(self.queue_linked_3.dequeue(), 1)
        self.assertEqual(self.queue_linked_3.dequeue(), 2)
        self.assertRaises(IndexError, self.queue_linked_3.dequeue)
        self.assertEqual(self.queue_linked_1.dequeue(), 1)
        self.assertEqual(self.queue_linked_1.dequeue(), 1)
        self.assertRaises(IndexError, self.queue_linked_1.dequeue)
        self.assertEqual(self.queue_linked_2.dequeue(), 1)
        self.assertEqual(self.queue_linked_2.dequeue(), 2)
        self.assertRaises(IndexError, self.queue_linked_1.dequeue)
        self.assertEqual(self.queue_linked_1, self.queue_linked_2)
        self.assertNotEqual(self.queue_linked_1, self.queue_linked_3)


    def test_queue_linked_is_empty_is_full_size(self):
        self.assertEqual(self.queue_linked_1.size(), 0)
        self.assertTrue(self.queue_linked_1.is_empty())
        self.assertFalse(self.queue_linked_1.is_full())
        self.queue_linked_1.enqueue(1)
        self.assertEqual(self.queue_linked_1.size(), 1)
        self.assertFalse(self.queue_linked_1.is_empty())
        self.assertFalse(self.queue_linked_1.is_full())
        self.queue_linked_1.enqueue(1)
        self.assertEqual(self.queue_linked_1.size(), 2)
        self.assertFalse(self.queue_linked_1.is_empty())
        self.assertTrue(self.queue_linked_1.is_full())
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.queue_linked_3.enqueue(1)
        self.assertEqual(self.queue_linked_3.size(), 5)
        self.assertFalse(self.queue_linked_3.is_empty())
        self.assertTrue(self.queue_linked_3.is_full())


    def test_queue_array_eq(self):
        self.assertNotEqual(self.queue_array_1, self.queue_array_3)
        self.assertEqual(self.queue_array_1, self.queue_array_2)
        self.queue_array_2.enqueue(2)
        self.assertNotEqual(self.queue_array_1, self.queue_array_2)
        self.queue_array_1.enqueue(2)
        self.assertEqual(self.queue_array_1, self.queue_array_2)


    def test_queue_array_repr(self):
        self.assertEqual(repr(self.queue_array_3), "QueueArray([]) Cap 5")
        self.assertEqual(repr(self.queue_array_1), "QueueArray([]) Cap 2")
        self.queue_array_1.enqueue(2)
        self.assertEqual(repr(self.queue_array_1),
                         "QueueArray([2]) Cap 2")
        self.queue_array_1.enqueue(2)
        self.assertEqual(repr(self.queue_array_1),
                         "QueueArray([2, 2]) Cap 2")


    def test_queue_array_enqueue(self):
        self.queue_array_1.enqueue(1)
        self.queue_array_2.enqueue(1)
        self.assertEqual(self.queue_array_1, self.queue_array_2)
        self.assertEqual(self.queue_array_1.size(), 1)
        self.queue_array_1.enqueue(1)
        self.queue_array_2.enqueue(2)
        self.assertNotEqual(self.queue_array_1, self.queue_array_2)
        self.assertEqual(self.queue_array_1.size(), 2)
        end = self.queue_array_2.write - 1
        self.assertEqual(self.queue_array_2.arr[end], 2)
        self.assertRaises(IndexError, self.queue_array_2.enqueue, 5)
        self.queue_array_2.dequeue()
        self.queue_array_2.dequeue()
        self.queue_array_2.enqueue(3)
        self.queue_array_2.enqueue(5)
        self.assertEqual(self.queue_array_2.write, 1) # Wrap around
        for i in range(self.queue_array_2.size()):
            self.queue_array_2.dequeue()
        self.assertEqual(self.queue_array_2.read, 1) # Wrap around


    def test_queue_array_dequeue(self):
        self.queue_array_1.enqueue(1)
        self.queue_array_2.enqueue(1)
        self.queue_array_1.enqueue(1)
        self.queue_array_2.enqueue(2)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(2)
        self.assertEqual(self.queue_array_3.dequeue(), 1)
        self.assertEqual(self.queue_array_3.dequeue(), 1)
        self.assertEqual(self.queue_array_3.dequeue(), 1)
        self.assertEqual(self.queue_array_3.dequeue(), 2)
        self.assertRaises(IndexError, self.queue_array_3.dequeue)
        self.assertEqual(self.queue_array_1.dequeue(), 1)
        self.assertEqual(self.queue_array_1.dequeue(), 1)
        self.assertRaises(IndexError, self.queue_array_1.dequeue)
        self.assertEqual(self.queue_array_2.dequeue(), 1)
        self.assertEqual(self.queue_array_2.dequeue(), 2)
        self.assertRaises(IndexError, self.queue_array_1.dequeue)
        self.assertEqual(self.queue_array_1, self.queue_array_2)
        self.assertNotEqual(self.queue_array_1, self.queue_array_3)


    def test_queue_array_is_empty_is_full_size(self):
        self.assertEqual(self.queue_array_1.size(), 0)
        self.assertTrue(self.queue_array_1.is_empty())
        self.assertFalse(self.queue_array_1.is_full())
        self.queue_array_1.enqueue(1)
        self.assertEqual(self.queue_array_1.size(), 1)
        self.assertFalse(self.queue_array_1.is_empty())
        self.assertFalse(self.queue_array_1.is_full())
        self.queue_array_1.enqueue(1)
        self.assertEqual(self.queue_array_1.size(), 2)
        self.assertFalse(self.queue_array_1.is_empty())
        self.assertTrue(self.queue_array_1.is_full())
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.queue_array_3.enqueue(1)
        self.assertEqual(self.queue_array_3.size(), 5)
        self.assertFalse(self.queue_array_3.is_empty())
        self.assertTrue(self.queue_array_3.is_full())


if __name__ == '__main__':
    unittest.main()
