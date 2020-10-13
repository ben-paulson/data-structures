"""Tests for expression evaluation
Author: Ben Paulson
"""

import unittest
from exp_eval import *


class ExpEvalTests(unittest.TestCase):

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval('2 3 2 ^ ^'), 512)
        self.assertEqual(postfix_eval('1 2 3 * +'), 7)
        self.assertEqual(postfix_eval('1 2 -3 * +'), -5) # Negative
        self.assertEqual(postfix_eval('1 2 3 - /'), -1)
        self.assertEqual(postfix_eval('5 1 2 + 4 ^ + 3 -'), 83)
        self.assertRaises(ValueError, postfix_eval, '1 0 /')
        # Too many operands
        self.assertRaises(PostfixFormatException, postfix_eval, '1 2 3 *')
        # Too few operands
        self.assertRaises(PostfixFormatException, postfix_eval, '1 2 * 3 - /')
        # Invalid tokens
        self.assertRaises(PostfixFormatException, postfix_eval, '5 3 h 2 >')


    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'),
                                          '3 4 2 * 1 5 - 2 3 ^ ^ / +')
        self.assertEqual(infix_to_postfix('( 3 + 6 ) * ( 2 - 4 ) + 7'),
                                          '3 6 + 2 4 - * 7 +')
        self.assertEqual(infix_to_postfix('( -3 + 6 ) * ( 2 - 4 ) + 7'),
                                          '-3 6 + 2 4 - * 7 +') # Negative
        self.assertEqual(infix_to_postfix('( 1 + 2 ) * 7'),
                                          '1 2 + 7 *')


    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix('^ 1 2'),
                                           '1 2 ^')
        self.assertEqual(prefix_to_postfix('^ -1 2'), # Negative
                                           '-1 2 ^')
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'),
                                           '3 2 1 / - 4 5 / 6 - *')
        self.assertEqual(prefix_to_postfix('- ^ + 4 2 6 ^ - 7 1 + 3 3'),
                                           '4 2 + 6 ^ 7 1 - 3 3 + ^ -')


if __name__ == '__main__':
    unittest.main()
