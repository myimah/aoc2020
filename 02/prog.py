from fileinput import input

inputs = []

for line in input("input.txt"):
    inputs.append(line)


def part1():
    valid_passwords = 0

    for inpt in inputs:
        min_v = int(inpt.split("-")[0])
        max_v = int(inpt.split("-")[1].split(" ")[0])
        letter = inpt.split(":")[0].split(" ")[1]
        password = inpt.split(":")[1]

        nb = password.count(letter)

        if min_v <= nb <= max_v:
            valid_passwords += 1

    return valid_passwords


def part2():
    valid_passwords = 0

    for inpt in inputs:
        pos_1 = int(inpt.split("-")[0])
        pos_2 = int(inpt.split("-")[1].split(" ")[0])
        letter = inpt.split(":")[0].split(" ")[1]
        password = inpt.split(":")[1].strip()

        if password[pos_1 - 1] == letter != password[pos_2 - 1] or password[pos_1 - 1] != letter == password[pos_2 - 1]:
            valid_passwords += 1

    return valid_passwords


print(f"part 1 : {part1()}")
print(f"part 2 : {part2()}")
