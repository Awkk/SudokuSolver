def init_grid(size):
    return [[i + j * size**2 for i in range(0, size**2)] for j in range(size**2)]


def print_grid(grid, size):
    print("----------------------------------------")
    for i in range(size):
        for j in range(size):
            row = []
            for subgrid in grid[i * size: i * size + size]:
                row.append("".join(["{:^4d}".format(num) for num in
                                    subgrid[j * size: j * size + size]]))
            print("|", end="")
            print("|".join(row), end="|\n")
            row.clear()
        print("----------------------------------------")


def main():
    size = 3
    grid = init_grid(size)
    print_grid(grid, size)


if __name__ == "__main__":
    main()
