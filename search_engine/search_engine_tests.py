"""Tests for basic search engine class
Author: Ben Paulson
"""

import unittest
from search_engine import SearchEngine
from hashtables import HashTableSepchain as HashTable, import_stopwords


class SearchEngineTests(unittest.TestCase):

    def setUp(self):
        self.dir = "docs"
        stopwords = import_stopwords("stop_words.txt", HashTable())
        self.se = SearchEngine(self.dir, stopwords)

    def test_read_file(self):
        self.assertEqual(len(self.se.read_file(f"{self.dir}/test.txt")), 1)
        self.assertEqual(len(self.se.read_file(
                         f"{self.dir}/information_retrieval.txt")), 3)
        self.assertEqual(len(self.se.read_file(
                         f"{self.dir}/hash_table.txt")), 7)
        self.assertEqual(len(self.se.read_file(
                         f"{self.dir}/data_structure.txt")), 5)


    def test_parse_words(self):
        se2 = SearchEngine(self.dir, [])
        lines = self.se.read_file(f"{self.dir}/hash_table.txt")
        self.assertNotEqual(self.se.parse_words(lines), se2.parse_words(lines))
        self.assertEqual(self.se.doc_length[f"{self.dir}\\test.txt"], 2)


    def test_search(self):
        self.assertEqual(self.se.search("Computer Science")[0][1], 1.0)
        self.assertEqual(str(self.se.search("hash table")[0][1])[:4], "0.06")
        self.assertEqual(str(self.se.search("ADT")[0][1])[:5], "0.017")
        self.assertEqual(str(self.se.search("ADT ADT")[0][1])[:5], "0.017")
        self.assertEqual(len(self.se.search("unix")), 0)


if __name__ == '__main__':
    unittest.main()
