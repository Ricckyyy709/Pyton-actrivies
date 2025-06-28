def rightmost_set_bit(n):
    """
    Checks if the rightmost set bit is in a number.

    Args:
        n: The number to check.

    Returns:
        The value of the rightmost set bit, or 0 if n is 0.
    """
    if n == 0:
        return 0
    return n & -n