"""Stack implementation with an array.
Author: Ben Paulson
"""

class StackArray:
    """An implementation of the stack data
    structure using an array of elements
    """
    def __init__(self):
        self.arr = [None] * 2
        self.capacity = 2
        self.num_items = 0


    def __eq__(self, other):
        return isinstance(other, StackArray) and self.arr == other.arr


    def __repr__(self):
        return f"StackArray({self.arr})"


    def push(self, item):
        """Add an element to the end of the stack
        Arguments:
            item (int): the item to add to the stack
        Returns:
            None
        """
        self.arr[self.num_items] = item
        self.num_items += 1
        self.check_for_resize()


    def pop(self):
        """Remove the top item in the stack.
        Returns:
            int: The item on top of the stack
        Raises:
            IndexError: if the stack is empty
        """
        if self.num_items == 0:
            raise IndexError("Cannot pop an empty stack")
        val = self.arr[self.num_items - 1]
        self.arr[self.num_items - 1] = None
        self.num_items -= 1
        self.check_for_resize()
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
        return self.arr[self.num_items - 1]


    def check_for_resize(self):
        """Check the size of the stack to see if
        its capacity needs to be enlarged or shrunk
        """
        if self.num_items == self.capacity:
            self.enlarge()
        elif self.num_items > 0 and self.capacity / self.num_items >= 4:
            self.shrink()


    def enlarge(self):
        """Double the capacity of the array by creating a
        new array with twice as many elements and copying
        the elements from self.arr to the new array
        """
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i, val in enumerate(self.arr):
            new_arr[i] = val
        self.arr = new_arr


    def shrink(self):
        """Halve the capacity of the array by creating a
        new array with half as many elements and copying
        the elements from self.arr to the new array
        """
        self.capacity //= 2
        new_arr = [None] * self.capacity
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
