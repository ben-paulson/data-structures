"""Linked list definition.
Author: Ben Paulson
"""

def add_helper(item, val, next_node, prev_node):
    """Helper function for OrderedList.add()
    Recursively adds an item in the case that 2+ items already exist
    and the item will not be the new head or tail of the list.
    Arguments:
        item (int): the item to add
        val (int): the value associated with the key item
        next_node (Node): the next node to check; insert item before this
        prev_node (Node): Node after which to insert the new item
    """
    if item < next_node.key:
        new_node = Node(item, val, next_node, prev_node)
        next_node.prev = new_node
        prev_node.next_elem = new_node
        return None
    return add_helper(item, val, next_node.next_elem, next_node)


def remove_helper(item, next_node, idx):
    """Helper function for OrderedList.remove()
    Recursively remove an item from the list by checking each
    node, starting from the head
    Arguments:
        item (int): the item to remove
        next_node (Node): the next node in the list
        idx (int): index of the current node being checked
    Returns:
        int: the index of the item, if found
    Raises:
        ValueError: if the item is not in the list
    """
    if next_node is None:
        raise ValueError("Item not found in list. Cannot remove.")
    if item == next_node.key:
        next_node.next_elem.prev = next_node.prev
        next_node.prev.next_elem = next_node.next_elem
        return idx
    return remove_helper(item, next_node.next_elem, idx + 1)


def search_helper(item, next_node, idx, direction, give_index=False):
    """Helper function for the following OrderedList methods:
        search_forward()
        search_backward()
        index()
    Recursively search each node in the list to determine if item exists in it
    Arguments:
        item (int): the item to find
        next_node (Node): the node being checked
        idx (int): the index of the item
        direction (int): the direction to traverse the list.
            If positive, search forward. Otherwise, search backward
        give_index (bool): False by default. A value of True will return the
            index of item if found, and raise ValueError if not.
    Returns:
        bool: True if item is found, False otherwise
    Raises:
        ValueError: if item is not found in list and give_index is True
    """
    if next_node is None:
        if give_index:
            raise ValueError("Item not in list")
        return False
    if item == next_node.key:
        if give_index:
            return idx
        return True
    if direction > 0:
        return search_helper(item, next_node.next_elem,
                             idx + 1, direction, give_index)
    return search_helper(item, next_node.prev,
                         idx - 1, direction, give_index)


def pop_helper(pos, next_node, idx, direction):
    """Helper function for OrderedList.pop()
    Removes an item from the end of the list or, if specified,
    from a specific index.
    Arguments:
        pos (int): the position of the item to remove
        next_node (Node): the node at index idx
        idx (int): the current index of the node being checked
        direction (int): if positive, search from head.
            Otherwise, search from tail
    """
    if pos == idx:
        key = next_node.key
        next_node.next_elem.prev = next_node.prev
        next_node.prev.next_elem = next_node.next_elem
        return key
    if direction > 0:
        return pop_helper(pos, next_node.next_elem, idx + 1, direction)
    return pop_helper(pos, next_node.prev, idx - 1, direction)


class OrderedList:
    """an ordered list
    Attributes:
        head (Node): a pointer to the head of the list
        tail (Node): a pointer to the tail of the list
        num_items (int): the number of items stored in the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0


    def __eq__(self, other):
        """Recursively check each node in both lists"""
        return isinstance(other, OrderedList) and self.head == other.head


    def __repr__(self):
        """Recursively get string representation of each node"""
        return self.head.__repr__()


    def add(self, item, val):
        """Add an item to the list while preserving order
        Time Complexity: O(n)
        Arguments:
            item (int): the item to add
            val (int): The value associated with key item
        Returns:
            None
        """
        if self.is_empty():
            new_node = Node(item, val, None, None)
            self.head = new_node
            self.tail = new_node
        elif self.num_items == 1:
            if item < self.head.key:
                new_node = Node(item, val, self.head, None)
                self.head = new_node
                self.tail.prev = new_node
            else:
                new_node = Node(item, val, None, self.head)
                self.head.next_elem = new_node
                self.tail = new_node
        else:
            if item < self.head.key:
                new_node = Node(item, val, self.head, None)
                self.head.prev = new_node
                self.head = new_node
            elif item > self.tail.key:
                new_node = Node(item, val, None, self.tail)
                self.tail.next_elem = new_node
                self.tail = new_node
            else:
                # Only need helper if new item is in the middle of the list
                add_helper(item, val, self.head.next_elem, self.head)
        self.num_items += 1


    def remove(self, item):
        """Removes the given item from the list
        Time Complexity: O(n)
        Arguments:
            item (int): the item to remove
        Returns:
            int: the index of the removed item
        Raises:
            ValueError: if the item does not exist in the list
        """
        if self.num_items == 0:
            raise ValueError("List must be nonempty to remove an item")
        if self.num_items == 1 and self.head.key == item:
            self.head = None
            self.tail = None
            self.num_items = 0
            return 0
        return_value = 0
        if item == self.head.key:
            if self.head is not None:
                self.head = self.head.next_elem
                self.head.prev = None
        elif item == self.tail.key:
            self.tail = self.tail.prev
            self.tail.next_elem = None
            return_value = self.num_items - 1
        else:
            return_value = remove_helper(item, self.head.next_elem, 1)
        self.num_items -= 1
        return return_value


    def search_forward(self, item):
        """Search the list for the given item
        Time Complexity: O(n)
        Arguments:
            item (int): the item to search for
        Returns:
            bool: True if item is in list, False otherwise
        """
        return search_helper(item, self.head, 0, 1)


    def search_backward(self, item):
        """Search the list for the given item
        Time Complexity: O(n)
        Arguments:
            item (int): the item to search for
        Returns:
            bool: True if item is in list, False otherwise
        """
        return search_helper(item, self.tail, self.num_items - 1, -1)


    def is_empty(self):
        """Checks if the list is empty
        Time Complexity: O(1)
        Returns:
            bool: True if list is empty, False otherwise
        """
        return self.head is None and self.tail is None


    def size(self):
        """The size of the list
        Time Complexity: O(1)
        Returns:
            int: number of items in the list
        """
        return self.num_items


    def index(self, item):
        """Find the index of the given item in the list
        Time Complexity: O(n)
        Arguments:
            item (int): the item to find the index of in the list
        Returns:
            int: index of the item, if found
        Raises:
            ValueError: if the item is not in the list
        """
        return search_helper(item, self.tail,
                             self.num_items - 1, -1, give_index=True)


    def pop(self, pos=None):
        """Remove an item from the end of the list,
        or from a certain position if specified.
        Time Complexity: O(n)
        Arguments:
            pos (int): Optional argument to specify the
            index of the item to be removed
        Returns:
            Node: the item that was removed from the list
        Raises:
            IndexError: if the index is out of range
        """
        if pos is not None:
            if pos >= self.num_items or pos < 0:
                raise IndexError("pop index out of range")
            if pos == 0:
                key = self.head.key
                self.remove(key)
                return key
            # If for some reason the last index is passed
            if pos == self.num_items - 1:
                end = self.tail.key
                self.remove(end)
                return end
            direction = -(pos - (self.num_items // 2))
            if direction > 0:
                key = pop_helper(pos, self.head, 0, direction)
                self.num_items -= 1
                return key
            key = pop_helper(pos, self.tail, self.num_items - 1, direction)
            self.num_items -= 1
            return key
        if self.num_items == 0:
            raise IndexError("pop index out of range")
        end = self.tail.key
        self.remove(end)
        return end


class Node:
    """A node of a list
    Attributes:
        key (str): the payload
        val (any): the value associated with the key
        next_elem (Node): the next item in the list
        prev (Node): the previous item in the list
    """
    def __init__(self, key, val, next_elem=None, prev=None):
        self.key = key
        self.val = val
        self.next_elem = next_elem
        self.prev = prev


    def __eq__(self, other):
        return (isinstance(other, Node) and self.key == other.key
                and self.next_elem == other.next_elem)


    def __repr__(self):
        return f"Node(key: {self.key}, val: {self.val}, {self.next_elem})"
