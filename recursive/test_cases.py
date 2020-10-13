"""Test cases
Author: Ben Paulson
"""

import unittest
import perm_gen_lex
import base_convert
import bear_picnic


class Project1Tests(unittest.TestCase):

    def test_perm_gen_lex(self):
        self.assertEqual(perm_gen_lex.perm_gen_lex("a"), ["a"])
        self.assertEqual(perm_gen_lex.perm_gen_lex("ab"), ["ab", "ba"])
        self.assertEqual(perm_gen_lex.perm_gen_lex("abc"),
            ["abc", "acb", "bac", "bca", "cab", "cba"])
        self.assertRaises(ValueError, perm_gen_lex.perm_gen_lex, 10)
        self.assertRaises(ValueError, perm_gen_lex.perm_gen_lex, "cba")


    def test_convert(self):
        self.assertEqual(base_convert.convert(10, 2), "1010")
        self.assertEqual(base_convert.convert(10, 10), "10")
        self.assertEqual(base_convert.convert(10, 16), "A")
        self.assertRaises(ValueError, base_convert.convert, -1, 5)
        self.assertRaises(ValueError, base_convert.convert, 35, 1)
        self.assertRaises(ValueError, base_convert.convert, 5, "f")


    def test_bears(self):
        self.assertTrue(bear_picnic.bears(250))
        self.assertTrue(bear_picnic.bears(42))
        self.assertFalse(bear_picnic.bears(53))
        self.assertFalse(bear_picnic.bears(41))
        self.assertRaises(ValueError, bear_picnic.bears, -1)
        self.assertRaises(ValueError, bear_picnic.bears, "59")


if __name__ == '__main__':
    unittest.main()
