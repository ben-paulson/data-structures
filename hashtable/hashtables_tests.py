"""Tests for the three implementations of hashtable
Author: Ben Paulson
"""

import unittest
import random
from hashtables import *
from linked_list import *


class HashTableTests(unittest.TestCase):

    def setUp(self):
        self.linear = HashTableLinear()
        self.quad = HashTableQuadratic()
        self.sepchain = HashTableSepchain()
        self.node = Node(4, 4, None, None)
        self.common_node = Node(4, 4, None, None)
        self.node1 = Node(10, self.common_node, None)
        self.node2 = Node(10, self.common_node, None)
        #self.node1.next = self.node2
        self.empty_list = OrderedList()
        self.empty_list2 = OrderedList()


    def test_eq_repr(self):
        self.assertNotEqual(self.linear, self.quad)
        self.assertEqual(self.linear, HashTableLinear())
        self.linear.put("hi", "hi")
        lin2 = HashTableLinear()
        lin2.put("hi", "hi")
        self.assertEqual(self.linear, lin2)
        self.assertEqual(repr(self.linear), "HashTableLinear([None, None, " +
                         "None, None, None, None, None, Node(key: hi, val: " +
                         "hi, None), None, None, None])")
        self.assertEqual(repr(self.quad), "HashTableQuadratic([None, " +
                         "None, None, None, None, None, None, None, None, " +
                         "None, None, None, None, None, None, None])")


    def test_put(self):
        self.assertRaises(KeyError, self.linear.get, "hi")
        self.assertRaises(KeyError, self.quad.get, "hi")
        self.assertRaises(KeyError, self.sepchain.get, "hi")
        self.assertFalse("hi" in self.linear)
        self.assertFalse("hi" in self.quad)
        self.assertFalse("hi" in self.sepchain)
        lin_sep_hash = self.linear.hash_string("hi")
        quad_hash = self.quad.hash_string("hi")
        self.linear.put("hi", "hi")
        self.quad.put("hi", "hi")
        self.sepchain.put("hi", "hi")
        self.assertEqual(self.linear.table[lin_sep_hash], Node("hi", "hi"))
        self.assertEqual(self.sepchain.table[lin_sep_hash].head,
                         Node("hi", "hi"))
        self.assertEqual(self.quad.table[quad_hash], Node("hi", "hi"))
        self.assertEqual(self.linear.num_items, 1)
        self.assertEqual(self.quad.num_items, 1)
        self.assertEqual(self.sepchain.num_items, 1)
        self.assertTrue(self.linear.contains("hi"))
        self.assertTrue(self.quad.contains("hi"))
        self.assertTrue(self.sepchain.contains("hi"))
        self.linear.put("hi", "hi")
        self.quad.put("hi", "hi")
        self.sepchain.put("hi", "hi")
        self.assertEqual(self.linear.table[lin_sep_hash], Node("hi", "hi"))
        self.assertEqual(self.sepchain.table[lin_sep_hash].head,
                         Node("hi", "hi"))
        self.assertEqual(self.quad.table[quad_hash], Node("hi", "hi"))
        self.assertEqual(self.linear.num_items, 1)
        self.assertEqual(self.quad.num_items, 1)
        self.assertEqual(self.sepchain.num_items, 1)
        self.assertEqual(self.linear.num_collisions, 0)
        self.assertEqual(self.quad.num_collisions, 0)
        self.assertEqual(self.sepchain.num_collisions, 0)
        lin_sep_hash = self.linear.hash_string("fklsljflseare")
        quad_hash = self.quad.hash_string("fklsljflseare")
        self.assertEqual(self.linear.hash_string("hello"), lin_sep_hash)
        self.linear["hello"] = "hello"
        self.linear.put("fklsljflseare", "fklsljflseare")
        self.assertEqual(self.linear.table[lin_sep_hash].key, "hello")
        # Plus 2 because "hi" is already in the next position
        self.assertEqual(self.linear.table[lin_sep_hash + 2].key,
                         "fklsljflseare")
        self.sepchain["hello"] = "hello"
        self.sepchain.put("fklsljflseare", "fklsljflseare")
        self.assertEqual(self.sepchain.table[lin_sep_hash].head.key,
                         "fklsljflseare")
        self.assertEqual(self.sepchain.table[lin_sep_hash].head.next_elem.key,
                         "hello")
        self.quad["hello"] = "hello"
        self.quad.put("fklsljflseare", "fklsljflseare")
        self.assertTrue(self.linear.contains("fklsljflseare"))
        self.assertTrue(self.quad.contains("fklsljflseare"))
        self.assertTrue(self.sepchain.contains("fklsljflseare"))
        self.assertEqual(self.quad.table[quad_hash].key, "hello")
        self.assertEqual(self.quad.table[quad_hash + 1].key,
                         "fklsljflseare")
        self.quad.put("slkff", "slkff")
        self.assertEqual(self.quad.hash_string("slkff"), quad_hash)
        self.assertEqual(self.quad.table[quad_hash + 4].key,
                         "slkff")
        self.assertEqual(self.linear.num_items, 3)
        self.assertEqual(self.quad.num_items, 4)
        self.assertEqual(self.sepchain.num_items, 3)
        self.assertEqual(self.linear.collisions(), 2)
        self.assertEqual(self.quad.collisions(), 3)
        self.assertEqual(self.sepchain.collisions(), 1)
        self.assertEqual(self.linear["hi"], "hi")
        self.assertEqual(self.quad["hi"], "hi")
        self.assertEqual(self.sepchain["hi"], "hi")
        self.assertEqual(self.sepchain.get("hello"), "hello")
        lin_cols = self.linear.collisions()
        self.assertEqual(self.linear.remove("hello").key, "hello")
        self.assertEqual(self.linear.table[lin_sep_hash].key, "fklsljflseare")
        self.assertEqual(self.linear.remove("fklsljflseare").key,
                         "fklsljflseare")
        self.assertEqual(self.linear.table[lin_sep_hash], None)
        self.assertRaises(KeyError, self.linear.remove, "fklsljflseare")
        self.assertEqual(self.linear.table[lin_sep_hash + 1].key, "hi")
        self.assertEqual(self.linear.remove("hi").key, "hi")
        self.assertEqual(self.linear, HashTableLinear())
        self.assertEqual(self.linear.size(), 0)
        self.assertEqual(self.linear.collisions(), lin_cols)
        sep_cols = self.sepchain.collisions()
        self.assertEqual(self.sepchain.remove("hello").key, "hello")
        self.assertEqual(self.sepchain.table[lin_sep_hash].head.key,
                         "fklsljflseare")
        self.sepchain.remove("fklsljflseare")
        self.assertIsNone(self.sepchain.table[lin_sep_hash].head)
        self.assertRaises(KeyError, self.sepchain.remove, "fklsljflseare")
        self.assertEqual(self.sepchain.table[lin_sep_hash + 1].head.key, "hi")
        self.sepchain.remove("hi")
        self.assertEqual(self.sepchain.size(), HashTableSepchain().size())
        self.assertEqual(self.sepchain.collisions(), sep_cols)


    def test_resize(self):
        self.assertEqual(self.linear.load_factor(), 0)
        self.assertEqual(self.quad.load_factor(), 0)
        self.assertEqual(self.sepchain.load_factor(), 0)
        linsize = self.linear.table_size
        quadsize = self.quad.table_size
        sepsize = self.sepchain.table_size
        for i in range(linsize):
            random_string = ""
            # make random string 5 characters long w/ random letters a-z
            for j in range(5):
                random_string += chr(random.randint(97, 123))
            if self.linear.table_size == linsize:
                self.assertEqual(self.linear.load_factor(), i / linsize)
            self.linear.put(random_string, random_string)
        self.assertEqual(self.linear.size(), linsize)
        for i in range(quadsize):
            random_string = ""
            # make random string 5 characters long w/ random letters a-z
            for j in range(5):
                random_string += chr(random.randint(97, 123))
            if self.quad.table_size == quadsize:
                self.assertEqual(self.quad.load_factor(), i / quadsize)
            self.quad.put(random_string, random_string)
        self.assertEqual(self.quad.size(), quadsize)
        for i in range(sepsize * 2):
            random_string = ""
            # make random string 5 characters long w/ random letters a-z
            for j in range(5):
                random_string += chr(random.randint(97, 123))
            if self.sepchain.table_size == sepsize:
                self.assertEqual(self.sepchain.load_factor(), i / sepsize)
            self.sepchain.put(random_string, random_string)
        self.assertEqual(self.sepchain.size(), sepsize * 2)
        self.assertEqual(self.quad.table_size, 32)
        self.assertEqual(self.linear.table_size, 23)
        self.assertEqual(self.sepchain.table_size, 23)


    def test_import_stopwords(self):
        linear = import_stopwords("stop_words.txt", HashTableLinear())
        quadratic = import_stopwords("stop_words.txt", HashTableQuadratic())
        sepchain = import_stopwords("stop_words.txt", HashTableSepchain())
        self.assertEqual(type(linear), HashTableLinear)
        self.assertEqual(type(quadratic), HashTableQuadratic)
        self.assertEqual(type(sepchain), HashTableSepchain)
        self.assertEqual(linear.size(), 305)
        self.assertEqual(quadratic.size(), 305)
        self.assertEqual(sepchain.size(), 305)


    def test_node_eq(self):
        self.assertEqual(self.common_node, self.common_node)
        self.assertEqual(self.node2, self.node1)
        self.assertEqual(self.node, self.common_node)
        self.assertNotEqual(self.node, self.node1)


    def test_node_repr(self):
        self.assertEqual(self.common_node.__repr__(),
                         "Node(key: 4, val: 4, None)")
        self.assertEqual(repr(self.empty_list), "None")


    def test_ordered_list_add(self):
        self.empty_list.add(1, 0)
        # Check that string repr is the same since they are not the same type
        # self.assertEqual(self.empty_list.__repr__(),
        #     Node(1, None, None).__repr__())
        self.empty_list.add(3, 0)
        # self.assertEqual(self.empty_list.__repr__(),
        #     "Node(1, Node(3, None))")
        self.empty_list2.add(2, 0)
        self.empty_list2.add(1, 0)
        # self.assertEqual(self.empty_list2.__repr__(),
        #     "Node(1, Node(2, None))")
        self.empty_list.add(0, 0)
        # self.assertEqual(self.empty_list.__repr__(),
        #     "Node(0, Node(1, Node(3, None)))")
        self.empty_list2.add(3, 0)
        # self.assertEqual(self.empty_list2.__repr__(),
        #     "Node(1, Node(2, Node(3, None)))")
        self.empty_list.add(2, 0)
        # self.assertEqual(self.empty_list.__repr__(),
        #     "Node(0, Node(1, Node(2, Node(3, None))))")
        self.assertNotEqual(self.empty_list, self.empty_list2)
        self.empty_list2.add(0, 0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(500, 0)
        self.assertNotEqual(self.empty_list, self.empty_list2)


    def test_ordered_list_is_empty(self):
        self.assertTrue(self.empty_list.is_empty())
        self.empty_list.add(3, 0)
        self.assertFalse(self.empty_list.is_empty())
        self.empty_list.add(5, 0)
        self.assertFalse(self.empty_list.is_empty())


    def test_ordered_list_remove(self):
        self.empty_list.add(3, 0)
        self.assertEqual(self.empty_list.remove(3), 0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(3, 0)
        self.empty_list.add(2, 0)
        self.empty_list2.add(3, 0)
        self.empty_list2.add(2, 0)
        self.empty_list.add(1, 0)
        self.assertEqual(self.empty_list.remove(1), 0)
        self.assertEqual(self.empty_list, self.empty_list2)
        self.empty_list.add(1, 0)
        self.assertEqual(self.empty_list.remove(3), 2)
        # self.assertEqual(self.empty_list.__repr__(),
        #     "Node(1, Node(2, None))")
        self.empty_list.add(3, 0)
        self.assertEqual(self.empty_list.remove(2), 1)
        # self.assertEqual(self.empty_list.__repr__(),
        #     "Node(1, Node(3, None))")
        self.empty_list.remove(1)
        self.empty_list.remove(3)
        self.assertRaises(ValueError, self.empty_list.remove, 3)
        self.empty_list.add(4, 0)
        self.assertRaises(ValueError, self.empty_list.remove, 6)
        self.empty_list.add(4, 0)
        self.empty_list.add(5, 0)
        self.empty_list.add(6, 0)
        self.empty_list.remove(5)


    def test_ordered_list_search_forward(self):
        for i in range(10):
            self.empty_list.add(i, 0)
        self.assertTrue(self.empty_list.search_forward(3))
        self.assertTrue(self.empty_list.search_forward(0))
        self.assertTrue(self.empty_list.search_forward(9))
        self.assertFalse(self.empty_list.search_forward(10))


    def test_ordered_list_search_backward(self):
        for i in range(10):
            self.empty_list.add(i, 0)
        self.assertTrue(self.empty_list.search_backward(3))
        self.assertTrue(self.empty_list.search_backward(0))
        self.assertTrue(self.empty_list.search_backward(9))
        self.assertFalse(self.empty_list.search_backward(10))


    def test_ordered_list_size(self):
        self.assertEqual(self.empty_list.size(), 0)
        self.empty_list.add(0, 0)
        self.assertEqual(self.empty_list.size(), 1)
        for i in range(1, 10):
            self.empty_list.add(i, 0)
        self.assertEqual(self.empty_list.size(), 10)


    def test_ordered_list_index(self):
        self.empty_list.add(0, 0)
        self.assertEqual(self.empty_list.index(0), 0)
        for i in range(1, 10):
            self.empty_list.add(i, 0)
        self.assertEqual(self.empty_list.index(9), 9)
        self.empty_list.add(15, 0)
        self.assertEqual(self.empty_list.index(15), 10)
        self.assertRaises(ValueError, self.empty_list.index, 100)


    def test_ordered_list_pop(self):
        for i in range(10):
            self.empty_list.add(i * 2, 0)
        self.assertEqual(self.empty_list.pop(), 18)
        for i in range(9):
            self.empty_list2.add(i * 2, 0)
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
            self.empty_list.add(i, 0)
        self.assertEqual(self.empty_list.pop(3), 3)


if __name__ == '__main__':
    unittest.main()
