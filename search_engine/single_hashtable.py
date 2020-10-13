"""Hashtable implementation, import stopwords function.
Author: Ben Paulson
"""

from linked_list import OrderedList


class HashTable:
    """HashTable implementation with linear probing
    """
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.resize_threshold = 1.5
        self.table = [None] * self.table_size
        self.num_items = 0
        self.num_collisions = 0


    def __eq__(self, other):
        return isinstance(other, type(self)) and self.table == other.table


    def __repr__(self):
        return f"{self.__class__.__name__}({self.table})"


    def __getitem__(self, key):
        """Get a value with [] notation instead of using .get()
        """
        return self.get(key)


    def __setitem__(self, key, data):
        """Enable assignment of a key/value pair with [] notation
        """
        return self.put(key, data)


    def __contains__(self, key):
        """Enable the use of the 'in' operator for hash tables
        """
        return self.contains(key)


    def hash_string(self, string):
        """Hashes a string into an integer index
        Arguments:
            string (str): The string to hash
            size (int): The size of the table
        Returns:
            int: The hashed string
        """
        _hash = 0
        for char in string:
            _hash = (_hash * 31 + ord(char)) % self.table_size
        return _hash


    def rehash(self, old_hash, i):
        """Rehash an old hash using one of either linear or quadratic probing
        techniques. Default is linear, quadratic rehash method is overridden
        in HashTableQuadratic class.
        Arguments:
            old_hash (int): The previous hashed index
            i (int): The number of iterations that the same
                     index has been rehashed
        Returns:
            int: The rehashed value
        """
        value = i // i
        return (old_hash + value) % self.table_size


    def resize(self):
        """Resize the table when the load factor becomes too large
        """
        self.table_size = (2 * self.table_size) + 1
        self.rehash_table()


    def keys(self):
        """Returns a list of all the keys in the hashtable
        Returns:
            list: All keys in the hash table
        """
        keys = []
        for pair in self.table:
            if pair is not None:
                pair = pair.head
                while pair is not None:
                    keys.append(pair.key)
                    pair = pair.next_elem
        return keys


    def size(self):
        """The size of the hash table.
        Returns:
            int: The number of items in the table
        """
        return self.num_items


    def load_factor(self):
        """The load factor 'a' of the hash table.
        Returns:
            int: The load factor of the table
        """
        return self.num_items / self.table_size


    def collisions(self):
        """The number of collisions that have occurred while inserting items
        Returns:
            int: The number of collisions for this hash table
        """
        return self.num_collisions


    def put(self, key, data):
        """Insert a key/val pair into the hash table. Override from parent
        class to work with linked list
        Arguments:
            key (str): The key to be inserted
            data (any): The value associated with the key
        """
        idx = self.hash_string(key)
        # Index has no Linked list
        if self.table[idx] is None:
            self.table[idx] = OrderedList()
            self.table[idx].add(key, data)
        # Linked list is there, either replace or add key to list
        else:
            self.num_collisions += 1
            if self.table[idx].search_forward(key):
                self.table[idx].remove(key) # Replace by deleting & re-adding
                self.num_items -= 1 # Essentially cancel out if item exists
                self.num_collisions -= 1 # same with collisions
            self.table[idx].add(key, data)
        self.num_items += 1
        if self.load_factor() >= self.resize_threshold:
            self.resize()


    def contains(self, key):
        """Checks if the hash map contains the given key.
        Override for Separate Chaining method
        Arguments:
            key (str): The key to check for
        Returns:
            bool: True if the key exists, False otherwise
        """
        for pair in self.table:
            if pair is not None and pair.search_forward(key):
                return True
        return False


    def remove(self, key):
        """Removes a key/val pair from the hash table. Separate chaining version
        Arguments:
            key (str): The key of the pair to remove
        Returns:
            Node: The key/val pair that was deleted
        """
        if not self.contains(key):
            raise KeyError(f"Cannot delete key {key} because it does not exist")
        idx = self.hash_string(key)
        node = self.table[idx].head
        while node.key != key:
            node = node.next_elem
        self.table[idx].remove(key)
        self.num_items -= 1
        return node


    def get(self, key):
        """Get the value of the key stored in the hash map. Override for
        separate chaining with linked list.
        Arguments:
            key (str): The key to search the value of
        Returns:
            any: The value associated with key
        Raises:
            KeyError: If the key is not found in the hash map
        """
        if not self.contains(key):
            raise KeyError("Key not found")
        node = self.table[self.hash_string(key)].head
        while node.key != key:
            node = node.next_elem
        return node.val


    def rehash_table(self):
        """Called only after the table is resized. Re-inserts every item
        in the old table with its new hashed value (due to the resize).
        Override for Separate Chaining method
        """
        old_table = self.table
        self.table = [None] * self.table_size
        self.num_items = 0
        for pair in old_table:
            if pair is not None:
                node = pair.head
                while node is not None:
                    self.put(node.key, node.val)
                    node = node.next_elem


class HashTableSepchain:
    pass

class HashTableLinear:
    pass

class HashTableQuadratic:
    pass


def import_stopwords(filename, hashtable):
    """Create a hashtable of words imported from filename
    Arguments:
        filename (str): Path to file that contains the words to be included
        hashtable (HashTable): An instance of any of the 3 hashtable classes
    Returns:
        HashTable: The hashtable filled with words from filename
    """
    with open(filename, 'r') as file:
        data = file.readlines()[0].split(' ')
        for word in data:
            hashtable.put(word, word)
    return hashtable
