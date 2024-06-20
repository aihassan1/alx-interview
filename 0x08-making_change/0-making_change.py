#!/usr/bin/python3
"""make a change problem"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    if coins == [] or coins == None:
        return -1

    try:
        coins.index(total)
        return 1
    except ValueError:
        pass

    min_ops = [total + 1 for total in range(total + 1)]
    min_ops[0] = 0

    coins.sort(reverse=True)

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                min_ops[i] = min(min_ops[i], min_ops[i - coin] + 1)

    return min_ops[total] if min_ops[total] != total + 1 else -1


print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
