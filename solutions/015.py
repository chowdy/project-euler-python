"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


# Builds a 2D array filled with 0's
def build_grid(x, y=None):
    if y is None:
        y = x
    grid = list(map((lambda i: [0] * y), range(0, x)))
    return grid


def solution():
    grid_size = 21
    grid = build_grid(grid_size)
    for row in grid:
        row[0] = 1
    for i, v in enumerate(grid[0]):
        grid[0][i] = 1

    for i, row in enumerate(grid):
        for j, v in enumerate(row):

            # Ignore the initial 1-value cells
            if v == 1:
                continue

            grid[i][j] = row[j-1] + grid[i-1][j]

    return grid[grid_size-1][grid_size-1]
