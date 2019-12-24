import math as m


def solve(grid):
    empty_row, empty_col = find_empty(grid)
    if empty_row == -1:
        return True
    for val in range(1, len(grid) + 1):
        if is_valid(grid, empty_row, empty_col, val):
            grid[empty_row][empty_col] = val
            if solve(grid):
                return True
            grid[empty_row][empty_col] = 0
    return False


def find_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if(grid[row][col] == 0):
                return (row, col)
    return (-1, -1)


def is_valid(grid, row, col, val):
    col_legal = all([grid[i][col] != val for i in range(len(grid))])
    if col_legal:
        row_legal = all([grid[row][i] != val for i in range(len(grid))])
        if row_legal:
            size = int(m.sqrt(len(grid)))
            subgrid_legal = all([grid[row//size * size + i][col//size * size + j] != val
                                 for i in range(size) for j in range(size)])
            if subgrid_legal:
                return True
    return False
