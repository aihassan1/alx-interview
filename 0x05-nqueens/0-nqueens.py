#!/usr/bin/python3
"""n queens"""

from sys import argv

N_queens = int(argv[1])


def check_existence_diagonal(list, position):
    """check if a number exists in a list"""
    return any(position == item for item in list)


def check_existence_vertical(list, position):
    """check existence"""
    return any(position == sublist[1] for sublist in list)


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)


if not isinstance(N_queens, int):
    print(type(N_queens))
    print("N must be a number")
    exit(code=1)

if N_queens < 4:
    print("N must be at least 4")
    exit(code=1)

valid_positions = []
positive_dig = []
negative_dig = []
chess_board = [[0 for i in range(N_queens)] for i in range(N_queens)]

for row in range(N_queens):
    for col in range(N_queens):
        if (
            check_existence_vertical(valid_positions, col)
            or check_existence_diagonal(positive_dig, row + col)
            or check_existence_diagonal(negative_dig, row - col)
        ):
            positive_dig.clear()
            negative_dig.clear()
            valid_positions.clear()

        positive_dig.append(row + col)
        negative_dig.append(row - col)
        valid_positions.append([row, col])
