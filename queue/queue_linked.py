"""Queue implementation with a linked list.
Author: Ben Paulson
"""

from node import Node


class QueueLinked:
    """Implementation of a Queue with a Linked List
    Attributes:
        capacity (int): Optional argument defining the max number of items
                        the queue can hold
    """
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.num_items = 0
        self.front = None
        self.rear = None


    def __eq__(self, other):
        return (isinstance(other, QueueLinked) and self.front == other.front
                and self.rear == other.rear and self.capacity == other.capacity
                and self.num_items == other.num_items)


    def __repr__(self):
        return f"QueueLinked({self.front}) Cap {self.capacity}"


    def dequeue(self):
        """Remove an item from the front of the queue
        Returns:
            int: The item removed from the queue
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty Queue")
        if self.num_items == 1:
            val = self.front.val
            self.front = None
            self.rear = None
        else:
            val = self.front.val
            self.front = self.front.next
        self.num_items -= 1
        return val


    def enqueue(self, item):
        """Add an item to the end of the queue
        Arguments:
            item (int): The item to add to the queue
        Raises:
            IndexError: If the queue is at full capacity
        """
        if self.is_full():
            raise IndexError("Cannot add an item to a full Queue")
        if self.is_empty():
            new_node = Node(item)
            self.rear = new_node
            self.front = new_node
        else:
            new_node = Node(item)
            self.rear.next = new_node
            self.rear = new_node
        self.num_items += 1


    def is_empty(self):
        """Checks if the queue is empty
        Returns:
            bool: True if queue is empty, False otherwise
        """
        return self.num_items == 0


    def is_full(self):
        """Checks if the queue is full
        Returns:
            bool: True if the queue is at capacity, False otherwise
        """
        return self.num_items == self.capacity


    def size(self):
        """The size of the queue
        Returns:
            int: The number of elements in the queue
        """
        return self.num_items
