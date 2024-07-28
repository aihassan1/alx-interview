#!/usr/bin/python3
"""make a change problem"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet
    a given amount total"""

    if total <= 0:
        return 0

    if total < 0 or type(total) is not int:
        return -1

    sorted_list = sorted(coins, reverse=True)
    denominations = []
    (sorted_list)
    while total > 0 and sorted_list:
        if (total - sorted_list[0]) >= 0:
            denominations.append(sorted_list[0])
            # print(total)
            # print(denominations)

            total = total - sorted_list[0]

        else:
            sorted_list = sorted_list[1:]

    if total != 0:
        # print("no denomination found")
        return -1

    return len(denominations)
