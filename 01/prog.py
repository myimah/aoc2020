from math import prod
import fileinput
from itertools import combinations

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(int(line))


def solve(goal=2020, nums=2):
    for combi in combinations(inputs, nums):
        if sum(combi) == goal:
            return prod(combi)


def part1():
    return solve()


def part2():
    return solve(nums=3)


print(f"part 1 : {part1()}")
print(f"part 2 : {part2()}")
