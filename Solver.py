import math as m


def init_grid(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    size = int(m.sqrt(len(grid)))
    for i in range(len(grid)):
        if i % size == 0:
            print("-" * len(grid) * 4 + "-" * (size + 1))
        row = grid[i]
        str_row = ["{:^4d}".format(num).replace("0", "0") for num in row]
        print("|", end="")
        print("|".join(["".join(str_row[i:i+size])
                        for i in range(0, len(grid), size)]), end="|\n")
    print("-" * len(grid) * 4 + "-" * (size + 1))


def solve(grid):
    if find_empty(grid) is None:
        pass


def find_empty(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if(grid[row][col] == 0):
                return (row, col)


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


def main():
    size = 9
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [
        4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    # grid = init_grid(size)
    print_grid(grid)


if __name__ == "__main__":
    main()
