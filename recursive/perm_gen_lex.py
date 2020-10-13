"""
Author: Ben Paulson
"""

def perm_gen_lex(string):
    """Generate a list of all permutations of the given string
    in lexicographic order.
    Args:
        string (str): The string to generate permutations of
    Returns:
        list: a list of all permutations of string in lexicographic order
    """
    # Input must be a string
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    perms = []
    # Base case
    if len(string) == 1:
        return [string]
    for i, _ in enumerate(string):
        # Make sure input is in lexicographic order already
        if i > 0 and string[i] < string[i - 1]:
            raise ValueError("Input string must be in lexicographic order")
        char_removed = string[:i] + string[i + 1:]
        small_perm = perm_gen_lex(char_removed) # recursion part
        # Add all combinations of this character and
        # permutations of the smaller string to the list
        for perm in small_perm:
            perms.append(string[i] + perm)
    return perms
