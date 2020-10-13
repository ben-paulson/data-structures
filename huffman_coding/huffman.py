"""Huffman Node definition.
Author: Ben Paulson
"""

class HuffmanNode:
    """Data definition for node of a huffman tree.
    Can be either a leaf node or an internal (including root) node.
    Attributes:
        char (str): The character value of the node
        freq (int): The number of times char occurs in the data
        left (HuffmanNode): Left subtree (can be None)
        right (HuffmanNode): Right subtree (can be None)
    """
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


    def __eq__(self, other):
        return (isinstance(other, HuffmanNode) and self.char == other.char and
                self.freq == other.freq and self.left == other.left and
                self.right == other.right)


    def __repr__(self):
        return (f"HuffmanNode({self.char}, {self.freq}, " +
                f"{self.left}, {self.right})")


    def __lt__(self, other):
        """Check if this HuffmanNode is less than another by comparing their
        frequencies, using ascii character values as a tiebreaker.
        """
        if self.freq == other.freq:
            return ord(self.char) < ord(other.char)
        return self.freq < other.freq
