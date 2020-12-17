import fileinput

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)


def count_around(pos_x, pos_y, pos_z, grid):
    count = 0
    for x in range(pos_x - 1, pos_x + 2, 1):
        for y in range(pos_y - 1, pos_y + 2, 1):
            for z in range(pos_z - 1, pos_z + 2, 1):
                if (x, y, z) in grid and (x, y, z) != (pos_x, pos_y, pos_z):
                    if grid[(x, y, z)] == "#":
                        count += 1
    return count


def part1():
    grid = {}

    for y in range(len(inputs)):
        for x in range(len(inputs[y])):
            grid[(x, y, 0)] = inputs[y][x]

    init_max_x = len(inputs)
    init_max_y = len(inputs[0])

    for i in range(1, 7):
        next_grid = {}
        for x in range(-i, init_max_x + i):
            for y in range(-i, init_max_y + i):
                for z in range(-i, i + 1):
                    c = count_around(x, y, z, grid)
                    if (x, y, z) in grid and grid[(x, y, z)] == "#":
                        if c == 2 or c == 3:
                            next_grid[(x, y, z)] = "#"
                    else:
                        if c == 3:
                            next_grid[(x, y, z)] = "#"
                        else:
                            next_grid[(x, y, z)] = "."
        grid = next_grid
    count = 0
    for pos in grid.values():
        if pos == "#":
            count += 1
    return count


def count_around_w(pos_x, pos_y, pos_z, pos_w, grid):
    count = 0
    for x in range(pos_x - 1, pos_x + 2, 1):
        for y in range(pos_y - 1, pos_y + 2, 1):
            for z in range(pos_z - 1, pos_z + 2, 1):
                for w in range(pos_w - 1, pos_w + 2, 1):
                    if (x, y, z, w) in grid and (x, y, z, w) != (pos_x, pos_y, pos_z, pos_w):
                        if grid[(x, y, z, w)] == "#":
                            count += 1
    return count


def part2():
    grid = {}

    for y in range(len(inputs)):
        for x in range(len(inputs[y])):
            grid[(x, y, 0, 0)] = inputs[y][x]

    init_max_x = len(inputs)
    init_max_y = len(inputs[0])

    for i in range(1, 7):
        next_grid = {}
        for x in range(-i, init_max_x + i):
            for y in range(-i, init_max_y + i):
                for z in range(-i, i + 1):
                    for w in range(-i, i + 1):
                        c = count_around_w(x, y, z, w, grid)
                        if (x, y, z, w) in grid and grid[(x, y, z, w)] == "#":
                            if c == 2 or c == 3:
                                next_grid[(x, y, z, w)] = "#"
                        else:
                            if c == 3:
                                next_grid[(x, y, z, w)] = "#"
                            else:
                                next_grid[(x, y, z, w)] = "."
        grid = next_grid

    count = 0
    for pos in grid.values():
        if pos == "#":
            count += 1
    return count


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
