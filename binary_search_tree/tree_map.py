"""Contains starter code

TreeMap implementation and application with classmates file

"""
import random
import bst
from classmate import classmate_factory


class TreeMap:
    """Implementation of a Binary Search Tree using a Map ADT.
    Attributes:
        tree (BSTNode): The root node of the tree
        num_items (int): The number of nodes in the tree
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return f"TreeMap({self.tree})"

    def __eq__(self, other):
        return isinstance(other, TreeMap) and self.tree == other.tree\
            and self.num_items == other.num_items

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return self.contains(key)

    def get(self, key):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with th key
        Raises:
            KeyError : if the key does not exist
        """
        return bst.get(self.tree, key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py and increments num_items by 1

        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.tree = bst.insert(self.tree, key, val)
        # Check if an item was actually inserted, or just replaced
        if len(bst.inorder_list(self.tree, [])) > self.num_items:
            self.num_items += 1

    def contains(self, key):
        """Checks if a certain key is in the tree
        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False
        """
        return bst.contains(self.tree, key)

    def delete(self, key):
        """Removes the key/value pair from the tree
        Args:
            key (any) : a key which is compareable by <,>,==
        Raises:
            KeyError : if the key does not exist
        """
        self.tree = bst.delete(self.tree, key)
        self.num_items -= 1

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self)->(any, any):
        """Finds the smallest key in the tree by calling find_min in bst
        Returns:
            tuple (any, any): Key/value pair of the smallest key in the tree
        """
        return bst.find_min(self.tree)

    def find_max(self)->(any, any):
        """Finds the largest key in the tree by calling find_max in bst
        Returns:
            tuple (any, any): Key/value pair of the largest key in the tree
        """
        return bst.find_max(self.tree)

    def inorder_list(self)->list:
        """Perform an inorder traversal of the list, returning the keys
        Returns:
            list (any): List of keys from inorder traversal of the tree.
                        Empty list if tree has no nodes
        """
        return bst.inorder_list(self.tree, [])

    def preorder_list(self)->list:
        """Perform a preorder traversal of the list, returning the keys
        Returns:
            list (any): List of keys from preorder traversal of the tree.
                        Empty list if tree has no nodes
        """
        return bst.preorder_list(self.tree, [])

    def tree_height(self)->int:
        """Find the height of the tree. Defined as the number of edges
        in the longest path to the leaf nodes.
        Returns:
            int: Height of the tree. -1 if empty
        """
        return bst.tree_height(self.tree)

    def range_search(self, low, high)->list:
        """Find a list of numbers in the tree that fall in a specific range.
        Arguments:
            lo (any): The lowest key (inclusive) in the range
                      of acceptable keys
            hi (any): The highest key (exclusive) in the range
                      of acceptable keys
        Returns:
            list (any, any): List of (key, value) tuples with keys in the range
        """
        return bst.range_search(self.tree, low, high, [])

def import_classmates(filename):
    """Imports classmates from a tsv file
    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    file = open(filename)
    lines = file.readlines()
    for line in lines:
        tokens = line.split('\t')
        classmate = classmate_factory(tokens)
        classmates.append(classmate)
    file.close()
    #shuffle the classmates
    random.seed(2)
    random.shuffle(classmates)
    for classmate in classmates:
        tree_map[classmate.sid] = classmate
    return tree_map

def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the sid as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    if sid not in tmap:
        raise KeyError(f"Classmate id {sid} does not exist")
    return tmap[sid]
