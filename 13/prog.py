import fileinput
import math

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)

arrival_time = int(inputs[0])
bus_ids = [int(b_id) for b_id in inputs[1].split(",") if b_id != "x"]


def part1():
    time = arrival_time
    first_time = 0
    while first_time == 0:
        for bus in bus_ids:
            if time % bus == 0:
                first_time = (time - arrival_time) * bus
        time += 1
    return first_time


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def part2():
    reqs = []
    for x in range(len(bus_ids)):
        reqs.append([x, bus_ids[x]])

    time = 0
    step = reqs[0][1]
    goodness = 1
    while goodness < len(reqs):
        req = reqs[goodness]
        offset = req[0]
        cycle = req[1]
        if (time + offset) % cycle == 0:
            step = lcm(step, cycle)
            goodness = goodness + 1
        else:
            time += step
    return time


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
