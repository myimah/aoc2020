import fileinput

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)


def gen_map(remove_number=False):
    bags_map = {}

    for ipt in inputs:
        holder, content = ipt.split("contain")

        holder = holder.replace("bags", "").strip()
        for col in content.split(","):
            if holder not in bags_map:
                bags_map[holder] = []
            if "no other" not in col:
                bags_map[holder].append(
                    col.replace("\n", "").replace("bags", "").replace("bag", "").replace(".", "").strip())
                if remove_number:
                    bags_map[holder][-1] = bags_map[holder][-1].split(" ", 1)[1]
    return bags_map


def present_inside(bags_map, color):
    bags = [color]
    for bag in bags_map:
        if color in bags_map[bag]:
            bags += present_inside(bags_map, bag)
    return bags


def count_inside_bag(bags_map, color):
    color = color.split(" ", 1)[1].strip()
    count = 1

    for bag in bags_map[color]:
        if bag != "no other":
            count += int(bag.split(" ", 1)[0]) * count_inside_bag(bags_map, bag)

    return count


def part1():
    return len(set(present_inside(gen_map(True), "shiny gold"))) - 1


def part2():
    return count_inside_bag(gen_map(), "1 shiny gold") - 1


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
