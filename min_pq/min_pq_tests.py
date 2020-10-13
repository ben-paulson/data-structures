"""MinPQ tests.
Author: Ben Paulson
"""

import unittest
from min_pq import MinPQ


class MinPQTests(unittest.TestCase):

    def setUp(self):
        self.pq1 = MinPQ()
        self.pq2 = MinPQ()


    def test_eq_repr(self):
        self.assertEqual(repr(self.pq1), 'MinPQ([None, None])')
        self.assertEqual(self.pq1, self.pq2)
        self.assertEqual(self.pq1.size(), 0)
        self.assertEqual(self.pq2.size(), 0)
        self.pq1.insert(0)
        self.pq1.insert(4)
        self.pq1.insert(3)
        self.pq2.insert(4)
        self.pq2.insert(3)
        self.pq2.insert(0)
        self.assertEqual(repr(self.pq1), 'MinPQ([0, 4, 3, None])')
        self.assertEqual(self.pq1.size(), 3)
        self.assertEqual(self.pq1.min(), 0)
        self.assertEqual(self.pq1, self.pq2)


    def test_heapify(self):
        pq = MinPQ([9, 6, 5, 2, 3])
        self.assertEqual(pq.arr, [2, 3, 5, 6, 9])
        pq = MinPQ([6, 3, 7, 2, 8, 1])
        self.assertEqual(pq.arr, [1, 2, 6, 3, 8, 7])
        pq = MinPQ([1, 3, 6, 8])
        self.assertEqual(pq.arr, [1, 3, 6, 8])


    def test_insert_del_size(self):
        self.assertRaises(IndexError, self.pq1.del_min)
        self.pq1.insert(1)
        self.assertEqual(self.pq1.size(), 1)
        self.assertEqual(self.pq1.arr, [1, None])
        self.pq1.insert(6)
        self.assertEqual(self.pq1.size(), 2)
        self.assertEqual(self.pq1.arr, [1, 6])
        self.pq1.insert(5)
        self.assertEqual(self.pq1.size(), 3)
        self.assertEqual(self.pq1.arr, [1, 6, 5, None])
        self.assertEqual(self.pq1.del_min(), 1)
        self.assertEqual(self.pq1.arr, [5, 6, None, None])
        self.pq1.insert(1)
        self.assertEqual(self.pq1.arr, [1, 6, 5, None])


    def test_1(self):
        pq = MinPQ()
        pq.insert(5)
        pq.insert(3)
        self.assertEqual(pq.capacity, 2)
        pq.insert(6)
        self.assertEqual(pq.size(), 3)
        self.assertTrue(pq.capacity == 4)
        self.assertEqual(pq.min(), 3)
        self.assertEqual(pq.del_min(), 3)
        self.assertEqual(pq.del_min(), 5)
        self.assertEqual(pq.del_min(), 6)
        self.assertEqual(pq.size(), 0)
        self.assertTrue(pq.is_empty())
        self.assertTrue(pq.capacity == 2)


    def test_2(self):
        pq = MinPQ([5, 4, 3, 2, 1])
        self.assertEqual(pq.size(), 5)
        self.assertTrue(pq.capacity == 5)
        self.assertTrue(pq.capacity == pq.num_items)
        self.assertTrue(pq.arr == [1, 2, 3, 5, 4])
        self.assertEqual(pq.min(), 1)
        self.assertEqual(pq.del_min(), 1)
        self.assertEqual(pq.del_min(), 2)
        self.assertEqual(pq.del_min(), 3)
        self.assertEqual(pq.del_min(), 4)
        self.assertEqual(pq.del_min(), 5)
        self.assertTrue(pq.capacity == 2)
        self.assertEqual(pq.size(), 0)
        self.assertTrue(pq.is_empty())


if __name__ == '__main__':
    unittest.main()
