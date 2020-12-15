import fileinput

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(int(line))


def part1():
    li = sorted(inputs)
    jolt_1 = 1
    jolt_3 = 1

    for i in range(1, len(li)):
        if li[i] - li[i - 1] == 1:
            jolt_1 += 1
        elif li[i] - li[i - 1] == 3:
            jolt_3 += 1

    return jolt_1, jolt_3, jolt_1 * jolt_3


max_value = max(inputs) + 3
paths = {}


def part2(last=0):
    num = 0
    if last in paths:
        return paths[last]

    paths[last] = []
    for i in range(1, 4):
        if last + i == max_value:
            return 1

        if last + i in inputs:
            num += part2(last + i)

    paths[last] = num
    return num


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
