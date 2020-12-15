import fileinput

inputs = [""]

for line in fileinput.input("input.txt"):
    if line == "\n":
        inputs.append("")
    else:
        inputs[-1] += line


def part1():
    nums = []

    for li in inputs:
        li = li.replace("\n", "").strip()
        nums.append(len(set(li)))
    return sum(nums)


def part2():
    nums = []

    for li in inputs:
        li = li.strip().split("\n")
        answers = []

        for i in range(len(li)):
            person = li[i]
            if i == 0:
                answers = person
            else:
                temp = []
                for p in person:
                    if p in answers:
                        temp.append(p)
                answers = temp

        nums.append(len(set(answers)))

    return sum(nums)


def part2Guibout():
    c = 0
    for group in inputs:
        base = set(group[0])

        for person in group[1:]:
            base = base.intersection(set(person))

        c += len(base)
    return c


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")