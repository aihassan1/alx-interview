#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """Calculate the minimum number of operations required to reach a given number.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required.

    """
    if n <= 1:
        return 0

    min_ops = 0
    factor = 2

    while n > 1:

        if n % factor == 0:
            min_ops += factor
            n = n // factor
        else:
            factor += 1

    return min_ops
