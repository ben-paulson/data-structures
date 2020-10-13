"""Queue implementation with an array.
Author: Ben Paulson
"""

class QueueArray:
    """An implementation of the queue data
    structure using an array of elements
    """
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.arr = [None] * (self.capacity + 1)
        self.num_items = 0
        self.read = 0
        self.write = 0


    def __eq__(self, other):
        return (isinstance(other, QueueArray) and
                self.arr[self.read:self.write] ==
                other.arr[other.read:other.write]
                and self.capacity == other.capacity
                and self.num_items == other.num_items)


    def __repr__(self):
        return (f"QueueArray({self.arr[self.read:self.write]}) " +
                f"Cap {self.capacity}")


    def dequeue(self):
        """Remove an item from the front of the queue
        Returns:
            int: The item removed from the queue
        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue an empty Queue")
        val = self.arr[self.read]
        self.arr[self.read] = None
        self.read += 1
        self.read %= len(self.arr)
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
        self.arr[self.write] = item
        self.write += 1
        self.write %= len(self.arr)
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
        return self.read == (self.write + 1) % len(self.arr)


    def size(self):
        """The size of the queue
        Returns:
            int: The number of elements in the queue
        """
        return self.num_items
