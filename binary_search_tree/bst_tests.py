"""Function tests for BST.
Author: Ben Paulson
"""

import unittest
from bst import *
from tree_map import *
from classmate import Classmate


class Lab5Tests(unittest.TestCase):

    def setUp(self):
        self.bst1 = TreeMap()
        self.bst2 = TreeMap()


    def test_bst_eq(self):
        self.assertEqual(self.bst1, self.bst2)
        self.bst1[1] = "1"
        self.bst2[1] = "1"
        self.assertEqual(self.bst1, self.bst2)
        self.bst1.delete(1)
        self.bst2.delete(1)
        self.assertEqual(self.bst1, self.bst2)


    def test_bst_insert(self):
        self.assertEqual(self.bst1.num_items, 0)
        self.assertEqual(repr(self.bst1), "TreeMap(None)")
        self.bst1[1] = "hello"
        self.assertEqual(self.bst1.num_items, 1)
        self.bst1[3] = "hi"
        self.assertEqual(self.bst1.num_items, 2)
        self.bst1[-2] = "-2"
        self.assertTrue(1 in self.bst1)
        self.bst1[-1] = "-1"
        self.bst1[-1] = "-2" # Value for key -1 replaced, no items added
        self.assertEqual(self.bst1.num_items, 4)


    def test_bst_delete(self):
        self.assertRaises(KeyError, self.bst1.delete, 1)
        self.bst1[70] = 1
        self.bst1[31] = 1
        self.bst1[14] = 1
        self.bst1[40] = 1
        self.bst1[23] = 1
        self.bst1[93] = 1
        self.bst1[73] = 1
        self.bst1[94] = 1
        self.assertEqual(repr(self.bst1), "TreeMap(BSTNode(key: 70, val: 1, " +
            "left: BSTNode(key: 31, val: 1, left: BSTNode(key: 14, val: 1, " +
            "left: None, right: BSTNode(key: 23, val: 1, left: None, right: " +
            "None)), right: BSTNode(key: 40, val: 1, left: None, right: None" +
            ")), right: BSTNode(key: 93, val: 1, left: BSTNode(key: 73, " +
            "val: 1, left: None, right: None), right: BSTNode(key: 94, " +
            "val: 1, left: None, right: None))))")
        self.bst1.delete(23)
        self.assertEqual(self.bst1.num_items, 7)
        self.assertIsNone(self.bst1.tree.left.left.right)
        self.bst1.delete(73)
        self.assertEqual(self.bst1.num_items, 6)
        self.assertIsNone(self.bst1.tree.right.left)
        self.bst1[23] = 1 # Add again
        self.bst1[73] = 1
        self.bst1.delete(14)
        self.assertEqual(self.bst1.num_items, 7)
        self.assertEqual(self.bst1.tree.left.left.key, 23)
        self.bst1.delete(40)
        self.assertEqual(self.bst1.num_items, 6)
        self.assertEqual(self.bst1.tree.left.left.key, 23)
        self.assertIsNone(self.bst1.tree.left.right)
        self.bst1.delete(70)
        self.assertEqual(self.bst1.tree.key, 73)
        self.assertIsNone(self.bst1.tree.right.left)
        self.assertEqual(self.bst1.num_items, 5)
        self.assertRaises(KeyError, self.bst1.delete, 10)
        self.bst2[70] = "70"
        self.bst2[60] = "60"
        self.bst2.delete(70)
        self.assertRaises(KeyError, self.bst2.get, 70)
        self.bst2[50] = "50"
        self.bst2[40] = "40"
        self.bst2.delete(50)
        self.assertEqual(self.bst2.size(), 2)
        self.assertEqual(self.bst2.tree.left.key, 40)


    def test_bst_contains_get(self):
        self.bst1[1] = "1"
        self.bst1[2] = "2"
        self.bst1[4] = "4"
        self.bst1[5] = "5"
        self.assertTrue(1 in self.bst1)
        self.assertTrue(5 in self.bst1)
        self.bst1.delete(1)
        self.assertFalse(1 in self.bst1)
        self.bst1[-2] = "-2"
        self.bst1[-3] = "-3"
        self.assertTrue(-2 in self.bst1)
        self.bst1.delete(-2)
        self.assertFalse(-2 in self.bst1)
        self.assertEqual(self.bst1[5], "5")
        self.assertEqual(self.bst1[4], "4")
        self.assertEqual(self.bst1[2], "2")
        self.assertRaises(KeyError, self.bst1.__getitem__, -2)


    def test_bst_find_min_max(self):
        self.assertRaises(ValueError, self.bst1.find_min)
        self.assertRaises(ValueError, self.bst1.find_max)
        self.bst1[1] = "1"
        self.bst1[2] = "2"
        self.bst1[4] = "4"
        self.bst1[5] = "5"
        self.bst1[-2] = "-2"
        self.bst1[-3] = "-3"
        self.assertEqual(self.bst1.find_min(), (-3, "-3"))
        self.assertEqual(self.bst1.find_max(), (5, "5"))
        self.bst1.delete(1)
        self.bst1.delete(-3)
        self.assertEqual(self.bst1.find_min(), (-2, "-2"))
        self.assertEqual(self.bst1.find_max(), (5, "5"))
        self.bst1.delete(2)
        self.bst1.delete(-2)
        self.bst1.delete(4)
        self.bst1.delete(5)
        self.assertRaises(ValueError, self.bst1.find_min)
        self.assertRaises(ValueError, self.bst1.find_max)


    def test_bst_inorder_list(self):
        self.assertEqual(self.bst1.inorder_list(), [])
        self.bst1[70] = 1
        self.bst1[31] = 1
        self.bst1[14] = 1
        self.bst1[40] = 1
        self.bst1[23] = 1
        self.bst1[93] = 1
        self.bst1[73] = 1
        self.bst1[94] = 1
        self.assertEqual(self.bst1.inorder_list(),
                         [14, 23, 31, 40, 70, 73, 93, 94])


    def test_bst_preorder_list(self):
        self.assertEqual(self.bst1.preorder_list(), [])
        self.bst1[70] = 1
        self.bst1[31] = 1
        self.bst1[14] = 1
        self.bst1[40] = 1
        self.bst1[23] = 1
        self.bst1[93] = 1
        self.bst1[73] = 1
        self.bst1[94] = 1
        self.assertEqual(self.bst1.preorder_list(),
                         [70, 31, 14, 23, 40, 93, 73, 94])


    def test_bst_tree_height(self):
        self.assertEqual(self.bst1.tree_height(), -1)
        self.bst1[70] = 1
        self.bst1[31] = 1
        self.bst1[14] = 1
        self.bst1[40] = 1
        self.bst1[23] = 1
        self.bst1[93] = 1
        self.bst1[73] = 1
        self.bst1[94] = 1
        self.assertEqual(self.bst1.tree_height(), 3)
        self.bst1.delete(23)
        self.assertEqual(self.bst1.tree_height(), 2)
        self.bst1.delete(14)
        self.assertEqual(self.bst1.tree_height(), 2)
        self.bst1.delete(40)
        self.bst1.delete(73)
        self.bst1.delete(94)
        self.assertEqual(self.bst1.tree_height(), 1)
        self.bst1.delete(31)
        self.bst1.delete(93)
        self.assertEqual(self.bst1.tree_height(), 0)
        self.bst1.delete(70)
        self.assertEqual(self.bst1.tree_height(), -1)


    def test_bst_range_search(self):
        self.assertEqual(self.bst1.range_search(23, 93), [])
        self.bst1[70] = 1
        self.bst1[31] = 1
        self.bst1[14] = 1
        self.bst1[40] = 1
        self.bst1[23] = 1
        self.bst1[93] = 1
        self.bst1[73] = 1
        self.bst1[94] = 1
        self.assertEqual(self.bst1.range_search(23, 93),
                         [(23, 1), (31, 1), (40, 1), (70, 1), (73, 1)])
        self.assertEqual(self.bst1.range_search(23, 94),
                         [(23, 1), (31, 1), (40, 1),
                          (70, 1), (73, 1), (93, 1)])
        self.assertEqual(self.bst1.range_search(14, 95),
                         [(14, 1), (23, 1), (31, 1), (40, 1),
                          (70, 1), (73, 1), (93, 1), (94, 1)])
        self.assertEqual(self.bst1.range_search(14, 16), [(14, 1)])


if __name__ == '__main__':
    unittest.main()
