import fileinput
from math import ceil

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)


def gen_ids(lines=127, columns=8):
    ids = []
    for place in inputs:
        li = 0
        column = 0
        upper_half = lines

        for i in range(7):
            upper_half /= 2
            if place[i] == "B":
                li += upper_half
        li = ceil(li)
        upper_half = columns
        for i in range(7, 10):
            upper_half /= 2
            if place[i] == "R":
                column += upper_half
        column = ceil(column)

        ids.append(li * 8 + column)
    return ids


generated_ids = gen_ids()


def part1():
    highest = 0
    for i in generated_ids:
        if i > highest:
            highest = i

    return highest


def part2():
    missing_id = 0
    for i in generated_ids:
        if i + 1 not in generated_ids and i + 2 in generated_ids:
            missing_id = i + 1
        elif i - 1 not in generated_ids and i - 2 in generated_ids:
            missing_id = i - 1

    return missing_id


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
