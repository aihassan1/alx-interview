#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """min ops func"""
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
