import fileinput
from itertools import product

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line.replace("\n", ""))


def part1():
    mem = {}
    current_mask = None
    for instr in inputs:
        if instr.startswith("mask"):
            current_mask = instr.split("=")[1]
        else:
            pos = int(instr.split("[")[1].split("]")[0])
            value = int(instr.split("=")[1])

            value_bin = bin(value).replace("b", "").zfill(len(current_mask))
            value_end = ""
            for i in range(len(value_bin)):
                if current_mask[i] != "X":
                    value_end += current_mask[i]
                else:
                    value_end += value_bin[i]
            mem[pos] = int(value_end, 2)

    return sum(mem.values())


def gen_addresses(pos_bin, mask):
    floating_points = []
    binary = ""
    for i in range(len(mask)):
        if mask[i] == "X":
            floating_points.append(i)
            binary += pos_bin[i]
        elif mask[i] == "0":
            binary += pos_bin[i]
        else:
            binary += mask[i]

    values = product(range(2), repeat=len(floating_points))

    addresses = []

    for val in values:
        new_bin = list(binary)
        for i in range(len(val)):
            new_bin[floating_points[i]] = val[i]
        addresses.append(int("".join([str(b) for b in new_bin]), 2))
    return addresses


def part2():
    mem = {}
    current_mask = None
    for instr in inputs:
        if instr.startswith("mask"):
            current_mask = instr.split("=")[1]
        else:
            pos = int(instr.split("[")[1].split("]")[0])
            value = int(instr.split("=")[1])

            pos_bin = bin(pos).replace("b", "").zfill(len(current_mask))

            memory_addresses = gen_addresses(pos_bin, current_mask)

            for addr in memory_addresses:
                mem[addr] = value

    return sum(mem.values())


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
