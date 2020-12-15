import fileinput

input_map = []

for line in fileinput.input("input.txt"):
    input_map.append(line.replace("\n", ""))


def part1(off_x, off_y):
    trees_encountered = 0
    x = 0
    y = 0
    while y < len(input_map):
        if input_map[y][x] == "#":
            trees_encountered += 1

        x = (x + off_x) % len(input_map[y])

        y += off_y

    return trees_encountered


def part2():
    return part1(1, 1) * part1(3, 1) * part1(5, 1) * part1(7, 1) * part1(1, 2)


print(f"Part 1: {part1(3, 1)}")
print(f"Part 2: {part2()}")
