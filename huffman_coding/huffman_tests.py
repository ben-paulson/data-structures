import unittest
import filecmp
from huffman import HuffmanNode
from huffman_coding import cnt_freq, create_huff_tree, create_code, huffman_encode, huffman_decode

class TestList(unittest.TestCase):

   def test_huffnode_eq_repr(self):
      huff1 = HuffmanNode('c', 5, None, None)
      huff2 = HuffmanNode('d', 5, None, None)
      self.assertNotEqual(huff1, huff2)
      huff2.char = 'c'
      self.assertEqual(huff1, huff2)
      self.assertEqual(repr(huff1), "HuffmanNode(c, 5, None, None)")

   def test_cnt_freq(self):
      freqlist  = cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 33)
      self.assertEqual(hufftree.left.char, 'd')
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 'd')
      right = hufftree.right
      self.assertEqual(right.freq, 17)
      self.assertEqual(ord(right.char), 0)

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      print('d', codes[ord('d')])
      print('a', codes[ord('a')])
      print('f', codes[ord('f')])
      self.assertEqual(codes[ord('d')], '0')
      self.assertEqual(codes[ord('a')], '11111')
      self.assertEqual(codes[ord('f')], '1110')

   def test_create_code2(self):
      freqlist = cnt_freq("file2.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      print('g', codes[ord('g')])
      print('o', codes[ord('o')])
      print(' ', codes[ord(' ')])
      self.assertEqual(codes[ord('g')], '00')
      self.assertEqual(codes[ord('o')], '01')
      self.assertEqual(codes[ord(' ')], '101')

   def test_create_code3(self):
      freqlist = cnt_freq("file3.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      print('s', codes[ord('s')])
      print('t', codes[ord('t')])
      print('a', codes[ord('a')])
      self.assertEqual(codes[ord('s')], '111')
      self.assertEqual(codes[ord('t')], '00')
      self.assertEqual(codes[ord('a')], '010')

   def test_empty(self):
       self.assertRaises(FileNotFoundError, huffman_decode,
                         "does_not_exist.txt", "dne_decode.txt")
       self.assertRaises(FileNotFoundError, huffman_encode,
                         "does_not_exist.txt", "dne_encode.txt")
       huffman_encode("empty.txt", "empty_encode.txt")
       self.assertTrue(filecmp.cmp("empty_encode.txt", "empty.txt"))

   def test_00(self):
      huffman_encode("file0.txt", "encodetest0.txt")
      self.assertTrue(filecmp.cmp("encodetest0.txt", "file0_soln.txt"))

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "encodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest1.txt", "file1_soln.txt"))

   def test_02_encodefile(self):
      huffman_encode("file2.txt", "encodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest2.txt", "file2_soln.txt"))

   def test_03_encodefile(self):
      huffman_encode("file3.txt", "encodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("encodetest3.txt", "file3_soln.txt"))

   def test_01_decodefile(self):
      huffman_decode("file1_soln_compressed.txt", "decodetest1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest1.txt", "file1.txt"))

   def test_02_decodefile(self):
      huffman_decode("file2_soln_compressed.txt", "decodetest2.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest2.txt", "file2.txt"))

   def test_03_decodefile(self):
      huffman_decode("file3_soln_compressed.txt", "decodetest3.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodetest3.txt", "file3.txt"))

   def test_04_decode_empty(self):
       huffman_decode("empty_encode_compressed.txt", "empty_decoded.txt")
       self.assertTrue(filecmp.cmp("empty_decoded.txt",
                                   "empty_encode_compressed.txt"))

   def test_05_decode_single_char(self):
      huffman_decode("encodetest0_compressed.txt", "decode_single.txt")
      self.assertTrue(filecmp.cmp("decode_single.txt",
                                  "file0.txt"))

if __name__ == '__main__':
   unittest.main()
