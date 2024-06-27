#!/usr/bin/python3
"""Island Perimeter"""


def check_four_dir(grid, x, y, land_param):
    """check the land in the 4 directions"""
    rows = len(grid)
    cols = len(grid[0])

    if x + 1 < rows and grid[x + 1][y] == 0:
        land_param.append((x + 1, y))

    if x - 1 >= 0 and grid[x - 1][y] == 0:
        land_param.append((x - 1, y))

    if y + 1 < cols and grid[x][y + 1] == 0:
        land_param.append((x, y + 1))

    if y - 1 >= 0 and grid[x][y - 1] == 0:
        land_param.append((x, y - 1))

    return land_param


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    land_param = []

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                land_param = check_four_dir(grid, x, y, land_param)

    return len(land_param)
