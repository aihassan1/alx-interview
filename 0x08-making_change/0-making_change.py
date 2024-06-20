#!/usr/bin/python3
"""make a change problem"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    min_ops = [total + 1 for total in range(total + 1)]
    min_ops[0] = 0
    coins = sorted(set(coins), reverse=True)

    for i in range(1, total + 1):
        for coin in coins:
            if coin > i:
                continue
            if i - coin == 0:
                min_ops[i] = 1
                break
            if i - coin >= 0:
                min_ops[i] = min(min_ops[i], min_ops[i - coin] + 1)

    return min_ops[total] if min_ops[total] != total + 1 else -1
