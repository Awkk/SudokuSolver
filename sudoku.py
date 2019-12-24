import backtracking_solver as bts
import math as m


def print_grid(grid):
    size = int(m.sqrt(len(grid)))
    for i in range(len(grid)):
        if i % size == 0:
            print("-" * len(grid) * 4 + "-" * (size + 1))
        row = grid[i]
        str_row = ["{:^4d}".format(num) if num !=
                   0 else "{:^4s}".format(" ") for num in row]
        print("|", end="")
        print("|".join(["".join(str_row[i:i+size])
                        for i in range(0, len(grid), size)]), end="|\n")
    print("-" * len(grid) * 4 + "-" * (size + 1))


def main():
    grid = [[0, 0, 5, 3, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 2, 0],
            [0, 7, 0, 0, 1, 0, 5, 0, 0],
            [4, 0, 0, 0, 0, 5, 3, 0, 0],
            [0, 1, 0, 0, 7, 0, 0, 0, 6],
            [0, 0, 3, 2, 0, 0, 0, 8, 0],
            [0, 6, 0, 5, 0, 0, 0, 0, 9],
            [0, 0, 4, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 9, 7, 0, 0]]

    grid2 = [[8, 5, 0, 0, 0, 2, 4, 0, 0],
             [7, 2, 0, 0, 0, 0, 0, 0, 9],
             [0, 0, 4, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 7, 0, 0, 2],
             [3, 0, 5, 0, 0, 0, 9, 0, 0],
             [0, 4, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 8, 0, 0, 7, 0],
             [0, 1, 7, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 3, 6, 0, 4, 0]]

    print("sudoku 1:")
    print_grid(grid)
    print("solution for sudoku 1:")
    if bts.solve(grid):
        print_grid(grid)
    else:
        print("No soultion found.")

    print("sudoku 2:")
    print_grid(grid2)
    print("solution for sudoku 2:")
    if bts.solve(grid2):
        print_grid(grid2)
    else:
        print("No soultion found.")


if __name__ == "__main__":
    main()
