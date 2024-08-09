#!/usr/bin/python3
def get_prime_numbs(n):
    """Function that gets the prime numbers list up to n."""
    if n < 2:
        return []

    nums_list = [True] * (n + 1)
    nums_list[0] = nums_list[1] = False

    for i in range(2, int(n**0.5) + 1):
        if nums_list[i]:
            for j in range(i * i, n + 1, i):
                nums_list[j] = False

    p_list = [i for i in range(n + 1) if nums_list[i]]

    return p_list


def isWinner(x, nums):
    """Define who is winner in a game."""
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria_score = 0
    ben_score = 0

    for number in nums:
        list_of_prime_nums = get_prime_numbs(number)
        moves = len(list_of_prime_nums)
        if moves % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif maria_score < ben_score:
        return "Ben"
    return None
