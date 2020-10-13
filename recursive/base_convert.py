"""
Author: Ben Paulson
"""

def convert(num, base):
    """Recursive function that returns a string representing
    num in the base given
    Args:
        num (int): non-negative base 10 integer which is the number to convert
        base (int): the base, between 2 and 16, to convert num to
    Returns:
        str: the string representing the num in the base given
    """
    # Check for valid arguments
    if not (isinstance(num, int) and isinstance(base, int)):
        raise ValueError("Both arguments must be integers")
    if num < 0:
        raise ValueError("Number to convert must be non-negative")
    if base > 16 or base < 2:
        raise ValueError("Base must be between 2 and 16")

    quotient = num // base
    remainder = num % base
    # Convert 10-16 to A-F for bases greater than 10
    if base > 10 and remainder >= 10:
        # Can reassign remainder since it is no longer used
        # for calculations in this function
        remainder = chr(remainder + 55)
    # Base case
    if quotient == 0:
        return str(remainder)
    return convert(quotient, base) + str(remainder)
