"""Minimum Priority Queue implementation with heap array.
Author: Ben Paulson
"""

class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): The capacity of the queue. The default capacity
                        is 2, but will be increased automatically.
        num_items (int): The number of items in the queue. This also points
                         to the position where a new item will be added.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, arr=None):
        """Initializes an object of MinPQ.
        Args:
            arr (list): The default value is None
        """
        if arr is None:
            self.capacity = 2
            self.arr = [None] * self.capacity
            self.num_items = 0
        else:
            self.arr = arr
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.heapify()


    def __eq__(self, other):
        return (isinstance(other, MinPQ) and
                self.arr[:self.num_items] == other.arr[:other.num_items])


    def __repr__(self):
        return f'MinPQ({self.arr})'


    def heapify(self):
        """Convert the array, self.arr, into a min heap.
        """
        start = (self.num_items - 2) // 2 # Parent of last item
        while start >= 0:
            self.shift_down(start)
            start -= 1


    def insert(self, item):
        """Inserts an item to the queue.
        Before inserting an item it checksif the array is full,
        if so, it enlarges the array by doubling the capacity.
        Args:
            item (any): An item to be inserted to the queue.
                        It is of any data type.
        """
        self.check_for_resize()
        self.arr[self.num_items] = item
        if self.num_items != 0:
            self.shift_up(self.num_items)
        self.num_items += 1


    def del_min(self):
        """Deletes the minimum item in the queue.
        After the deletion and just before returning the removed item,
        it checks if the array needs to be shrinked.
        If so, it downsizes the array by halving the capacity.
        Returns:
            any: it returns the minimum item, which has just been deleted.
        Raises:
            IndexError: Raises IndexError when the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot remove item from empty queue")
        val = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.arr[self.num_items - 1] = None
        self.num_items -= 1
        self.shift_down(0)
        self.check_for_resize()
        return val


    def min(self):
        """Returns the minimum item in the queue without deleting the item.
        Returns:
            any: It returns the minimum item.
        Raises:
            IndexError: Raises IndexError when the queue is empty.
        """
        return self.arr[0]


    def is_empty(self):
        """Checks if the queue is empty.
        Returns:
            bool: True if empty, False otherwise.
        """
        return self.num_items == 0


    def size(self):
        """Returns the number of items in the queue.
        Returns:
            int: It returns the number of items, self.num_items, in the queue.
        """
        return self.num_items


    def shift_up(self, idx):
        """Shifts up an item in the queue using tail recursion.
        Args:
            idx (int): the index of the item to be shifted up in the array.
        """
        parent_idx = (idx - 1) // 2
        if parent_idx < 0:
            return
        if self.arr[idx] < self.arr[parent_idx]:
            temp = self.arr[parent_idx]
            self.arr[parent_idx] = self.arr[idx]
            self.arr[idx] = temp
            self.shift_up(parent_idx)


    def shift_down(self, idx):
        """Shifts down an item in the queue using tail recursion.
        Args:
            idx (int): The index of the item to be shifted down in the array.
        """
        left = 2 * idx + 1
        right = 2 * idx + 2
        shift_idx = None
        # If no children
        if self.num_items - 1 < left and self.num_items - 1 < right:
            return
        # Only one child
        if self.num_items - 1 < right and not self.num_items - 1 < left:
            shift_idx = left
        # 2 Children, find min
        else:
            if self.arr[left] < self.arr[right]:
                shift_idx = left
            else:
                shift_idx = right
        # Make sure the value at shift index is lower than this one
        if self.arr[shift_idx] < self.arr[idx]:
            temp = self.arr[idx]
            self.arr[idx] = self.arr[shift_idx]
            self.arr[shift_idx] = temp
            self.shift_down(shift_idx)


    def check_for_resize(self):
        """Check the size of the stack to see if
        its capacity needs to be enlarged or shrunk
        """
        if self.num_items > 0:
            if self.num_items == self.capacity:
                self.enlarge()
            elif self.capacity / self.num_items >= 4:
                self.shrink()


    def enlarge(self):
        """Enlarges the array
        """
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i, val in enumerate(self.arr):
            new_arr[i] = val
        self.arr = new_arr


    def shrink(self):
        """Shrinks the array
        """
        self.capacity //= 2
        new_arr = [None] * self.capacity
        for i in range(self.num_items):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
