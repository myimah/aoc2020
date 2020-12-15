import fileinput
import re

inputs = [""]

for line in fileinput.input("input.txt"):
    if line == "\n":
        inputs.append("")
    else:
        inputs[-1] += line.replace("\n", " ")


def part1():
    keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    valid = 0
    for ipt in inputs:
        pk = 0

        for key in keys:
            if key in ipt:
                pk += 1
        if pk == len(keys):
            valid += 1
    return valid


def part2():
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid = 0

    for ipt in inputs:
        pk = 0

        fields = ipt.strip().split(" ")

        for field in fields:
            key, value = field.split(":")

            if key == "byr":
                if 1920 <= int(value) <= 2002:
                    pk += 1
            elif key == "iyr":
                if 2010 <= int(value) <= 2020:
                    pk += 1
            elif key == "eyr":
                if 2020 <= int(value) <= 2030:
                    pk += 1
            elif key == "hgt":
                if value.endswith("cm"):
                    height = value.replace("cm", "")
                    if 150 <= int(height) <= 193:
                        pk += 1
                if value.endswith("in"):
                    height = value.replace("in", "")
                    if 59 <= int(height) <= 76:
                        pk += 1
            elif key == "hcl":
                if re.match("^#([a-f0-9]{6})$", value):
                    pk += 1
            elif key == "ecl":
                if value in eye_colors:
                    pk += 1
            elif key == "pid":
                if re.match("^[0-9]{9}$", value):
                    pk += 1

        if pk == 7:
            valid += 1

    return valid


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
