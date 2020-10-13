"""Module for BST

Contains the data definition of BST,
and functions (not class member methods) on BST.

Functions defined here need to be recusrive functions,
and will be used by other classes such as TreeMap as
helper functions.


Author:
    Ben Paulson
"""

class BSTNode:
    """ Binary Search Tree is one of
    - None
    - BSTNode

    Attributes:
        key (any): key
        val (any): value associated with the key
        left (BSTNode): left subtree of Binary Search Tree
        right (BSTNode): right subtree of Binary Search Tree
    """
    def __init__(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return isinstance(other, BSTNode) and self.key == other.key\
            and self.val == other.val and self.left == other.left\
            and self.right == other.right

    def __repr__(self):
        return f"BSTNode(key: {self.key}, val: {self.val}, " +\
            f"left: {self.left}, right: {self.right})"

def get(tree, key)->any:
    """Get the value of the node that has key from tree
    Arguments:
        tree (BSTNode): The start node in the tree to check
        key (any): The key to get the value of
    Returns:
        any: The value of the node with key key
    Raises:
        KeyError: If the key does not exist in the tree
    """
    if tree is None:
        raise KeyError("Key not in tree")
    if tree.key == key:
        return tree.val
    if key < tree.key:
        return get(tree.left, key)
    return get(tree.right, key)

def contains(tree, key)->bool:
    """Check if key exists in tree
    Arguments:
        tree (BSTNode): The start node in the tree to check
        key (any): The key to check if exists in tree
    Returns:
        bool: The value of the node with key key
    """
    if tree is None:
        return False
    if tree.key == key:
        return True
    if key < tree.key:
        return contains(tree.left, key)
    return contains(tree.right, key)


def insert(tree, key, val)->BSTNode:
    """Insert the key/value pair in the tree
    Arguments:
        tree (BSTNode): The start node in the tree to check
        key (any): The key comparable by < > ==
        val (any): The value associated with key
    Returns:
        BSTNode: the node that was inserted
    """
    if tree is None:
        return BSTNode(key, val, None, None)
    if tree.key == key:
        tree.val = val
    elif key < tree.key:
        tree.left = insert(tree.left, key, val)
    else:
        tree.right = insert(tree.right, key, val)
    return tree

def delete(tree, key)->BSTNode:
    """Removes the key/value pair from the tree
    Args:
        tree (BSTNode): The start of the tree to delete the key from
        key (any) : a key which is compareable by <,>,==
    Raises:
        KeyError : if the key does not exist
    """
    return delete_helper(tree, key, None)

def delete_helper(tree, key, parent):
    """Helper function for delete. Removes the key/value pair from the tree
    Args:
        tree (BSTNode): The start of the tree to delete the key from
        key (any) : a key which is compareable by <,>,==
        parent (BSTNode): The parent of the current node
    Raises:
        KeyError : if the key does not exist
    """
    if not contains(tree, key):
        raise KeyError("Key not found")
    if key == tree.key:
        # Case 1: leaf node
        if tree.left is None and tree.right is None:
            if parent is not None:
                if tree.key > parent.key:
                    parent.right = None
                else:
                    parent.left = None
            tree = None
        # Case 2: 1 child
        elif (tree.left is None and tree.right is not None) or\
           (tree.right is None and tree.left is not None):
            if parent is not None:
                if tree.key > parent.key:
                    if tree.left is None:
                        parent.right = tree.right
                    else:
                        parent.right = tree.left
                else:
                    if tree.left is None:
                        parent.left = tree.right
                    else:
                        parent.left = tree.left
            else:
                if tree.left is None:
                    tree = tree.right
                else:
                    tree = tree.left
                parent = tree
        # Case 3: 2 children
        else:
            val = tree.right.left
            if val is None: # Get parent of intended neighbor if the intended
                val = tree.right # one does not exist
            delete_helper(tree, val.key, parent)
            tree.key = val.key
            tree.val = val.val
    elif key < tree.key:
        delete_helper(tree.left, key, tree)
    else:
        delete_helper(tree.right, key, tree)
    return tree

def find_min(tree)->(any, any):
    """Finds the smallest key in the tree
    Arguments:
        tree (BSTNode): The tree to traverse
    Returns:
        tuple (any, any): Key/value pair of the smallest key in the tree
    """
    if tree is None:
        raise ValueError("Tree is empty")
    if tree.left is None:
        return tree.key, tree.val
    return find_min(tree.left)

def find_max(tree)->(any, any):
    """Finds the largest key in the tree
    Arguments:
        tree (BSTNode): The tree to traverse
    Returns:
        tuple (any, any): Key/value pair of the largest key in the tree
    """
    if tree is None:
        raise ValueError("Tree is empty")
    if tree.right is None:
        return tree.key, tree.val
    return find_max(tree.right)

def inorder_list(tree, accum):
    """Perform an inorder traversal of the list, returning the keys
    Arguments:
        tree (BSTNode): The start node of the tree to traverse
        accum (list): List of keys found in the inorder traversal
    Returns:
        list (any): List of keys from inorder traversal of the tree.
                    Empty list if tree has no nodes
    """
    if tree is None:
        return []
    if tree.left is not None:
        inorder_list(tree.left, accum)
    accum.append(tree.key)
    if tree.right is not None:
        inorder_list(tree.right, accum)
    return accum

def preorder_list(tree, accum):
    """Perform a preorder traversal of the list, returning the keys
    Arguments:
        tree (BSTNode): The start node of the tree to traverse
        accum (list): List of keys found in the preorder traversal
    Returns:
        list (any): List of keys from preorder traversal of the tree.
                    Empty list if tree has no nodes
    """
    if tree is None:
        return []
    accum.append(tree.key)
    if tree.left is not None:
        preorder_list(tree.left, accum)
    if tree.right is not None:
        preorder_list(tree.right, accum)
    return accum

def tree_height(tree)->int:
    """Find the height of the tree. Defined as the number of edges
    in the longest path to the leaf nodes.
    Arguments:
        tree (BSTNode): Start node of the tree
    Returns:
        int: Height of the tree. -1 if empty
    """
    if tree is None:
        return -1
    if tree.left is None and tree.right is None:
        return 0
    right_depth = tree_height(tree.right) + 1
    left_depth = tree_height(tree.left) + 1
    return max(right_depth, left_depth)


def range_search(tree, low, high, accum):
    """Find a list of numbers in the tree that fall in a specific range.
    Arguments:
        tree (BSTNode): the head of the tree to search
        low (any): The lowest key (inclusive) in the range of acceptable keys
        high (any): The highest key (exclusive) in the range of acceptable keys
        accum (list): List of (key, value) tuples with keys in the range
    Returns:
        list (any, any): List of (key, value) tuples with keys in the range
    """
    if tree is None:
        return []
    # Do not search unnecessary nodes
    if tree.key < low:
        range_search(tree.right, low, high, accum)
    if tree.key >= high:
        range_search(tree.left, low, high, accum)
    if tree.key < high and tree.key >= low: # In range
        range_search(tree.left, low, high, accum)
        accum.append((tree.key, tree.val)) # Add in-order
        range_search(tree.right, low, high, accum)
    return accum
