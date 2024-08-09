# create function the gets the prime numbers list up to n


def get_prime_numbs(n):
    "function the gets the prime numbers list up to n"

    nums_list = [True] * (n + 1)
    nums_list[0] = nums_list[1] = False

    for i in range(2, int(n**0.5) + 1):
        if nums_list[i] is True:
            for j in range(i * i, n + 1, i):
                nums_list[j] = False

    p_list = [i for i in range(n + 1) if nums_list[i]]

    return p_list


def isWinner(x, nums):
    """define who is winner in a game"""
    Maria_score = 0
    Ben_Score = 0

    for number in nums:
        list_of_prime_nums = get_prime_numbs(number)
        if len(list_of_prime_nums) % 2 == 0:
            Ben_Score += 1

        else:
            Maria_score += 1

    if Maria_score > Ben_Score:
        return "Maria"
    elif Maria_score < Ben_Score:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
