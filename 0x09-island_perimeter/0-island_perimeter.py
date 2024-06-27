#!/usr/bin/python3
"""Island Perimeter"""


def count_water_around_land(grid, x, y, land_param):
    """check the land in the 4 directions"""
    rows = len(grid)
    cols = len(grid[0])

    # handel corners
    if x - 1 < 0:
        land_param.append(("top land"))
    if x + 1 > rows:
        land_param.append(("bottom land"))
    if y + 1 > cols:
        land_param.append(("right land"))
    if y - 1 < 0:
        land_param.append(("left land"))

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
                land_param = count_water_around_land(grid, x, y, land_param)

    return (land_param)
