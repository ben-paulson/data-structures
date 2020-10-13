"""Stack implementation with a singly linked list.
Author: Ben Paulson
"""

from node import Node


class StackLinked:
    """An implementation of the stack data
    structure using a singly linked list
    """
    def __init__(self):
        self.top = None
        self.num_items = 0


    def __eq__(self, other):
        return isinstance(other, StackLinked) and self.top == other.top


    def __repr__(self):
        return f'StackLinked({self.top})'


    def push(self, item):
        """Add an element to the end of the stack
        Arguments:
            item (int): the item to add to the stack
        Returns:
            None
        """
        new_top = Node(item, nxt=self.top)
        self.top = new_top
        self.num_items += 1


    def pop(self):
        """Remove the top item in the stack.
        Returns:
            int: The value on top of the stack
        Raises:
            IndexError: if the stack is empty
        """
        if self.num_items == 0:
            raise IndexError("Cannot pop an empty stack")
        val = self.top.val
        self.top = self.top.next
        self.num_items -= 1
        return val


    def is_empty(self):
        """Check if the stack is empty
        Returns:
            bool: True if empty, False otherwise
        """
        return self.num_items == 0


    def size(self):
        """Size of the stack
        Returns:
            int: number of items in the stack
        """
        return self.num_items


    def peek(self):
        """Check the value on the top of the stack
        Returns:
            int: The top item on the stack, if available.
                 If not available, return None
        Raises:
            IndexError: If the stack is empty
        """
        if self.num_items == 0:
            raise IndexError("Stack is empty")
        return self.top.val
