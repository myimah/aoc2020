import fileinput
from itertools import combinations

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(int(line))


def part1(n=25):
    for i in range(n, len(inputs)):
        num = inputs[i]
        valid = False
        for combi in combinations(inputs[i - n:i], 2):
            if sum(combi) == num:
                valid = True
                break
        if not valid:
            return num
    return 0


def part2(to_find):
    for i in range(2, len(inputs)):
        for j in range(0, len(inputs), 1):
            chunk = inputs[j:j + i]
            if sum(chunk) == to_find:
                return max(chunk) + min(chunk)
        i += 1
    return 0


part1_invalid = part1()
print(f"part 1 : {part1_invalid}")
print(f"part 2 : {part2(part1_invalid)}")
