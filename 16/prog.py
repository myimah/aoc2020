import fileinput
from itertools import permutations

fields = {}
your_ticket = []
tickets = []
t = 0

for line in fileinput.input("input.txt"):
    line = line.replace("\n", "")
    if line == '':
        t += 1
        continue
    if t == 0:
        name, ranges = line.split(":")
        ranges = ranges.split(" or ")
        r = []
        for ra in ranges:
            r.append([int(i) for i in ra.split("-")])
        fields[name] = r
    elif t == 1:
        if line != "your ticket:":
            your_ticket = [int(i) for i in line.split(",")]
    elif t == 2:
        if line != "nearby tickets:":
            tickets.append([int(i) for i in line.split(",")])

tickets.append(your_ticket)

invalid_tickets = []


def part1():
    error_rate = 0
    for ticket in tickets:
        for i in range(len(ticket)):
            valid = False
            for field_ranges in fields.values():
                for field_range in field_ranges:
                    if field_range[0] <= ticket[i] <= field_range[1]:
                        valid = True
            if not valid:
                error_rate += ticket[i]
                invalid_tickets.append(ticket)
    return error_rate


def check(field, pos):
    field_range = fields.get(field)
    for ticket in tickets:
        if ticket in invalid_tickets:
            continue
        if not (field_range[0][0] <= ticket[pos] <= field_range[0][1] or field_range[1][0] <= ticket[pos] <=
                field_range[1][1]):
            return False
    return True


paths = []
works_for = {}


def part2():
    for field in fields.keys():
        for i in range(len(fields.keys())):
            if check(field, i):
                if i not in works_for.keys():
                    works_for[i] = []
                works_for[i].append(field)

    valid_order = [""] * len(fields.keys())

    while "" in valid_order:
        for i in range(len(valid_order)):
            if valid_order[i] == "":
                valid_fields = set()
                for field in works_for[i]:
                    if field not in valid_order:
                        valid_fields.add(field)
                if len(valid_fields) == 1:
                    valid_order[i] = valid_fields.pop()
    f = 1
    for i in range(len(valid_order)):
        if valid_order[i].startswith("departure"):
            f *= your_ticket[i]
    return f


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
