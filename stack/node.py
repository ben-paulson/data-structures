"""Node definition.
Author: Ben Paulson
"""

class Node:
    """A node of a list
    Attributes:
        val (int): the payload
        nxt (Node): the next item in the list
        prev (Node): the previous item in the list
    """
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


    def __eq__(self, other):
        return (isinstance(other, Node) and self.val == other.val
                and self.next == other.next)


    def __repr__(self):
        return f"Node({self.val}, {self.next})"
