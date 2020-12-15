import fileinput

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)


def run(program, return_value=False):
    i = 0
    acc = 0
    instru = []
    failed = False
    while True:
        if i in instru:
            failed = True
            break

        instru.append(i)

        if program[i].startswith("nop"):
            i += 1
        elif program[i].startswith("jmp"):
            i += int(program[i].split(" ")[1])
        elif program[i].startswith("acc"):
            acc += int(program[i].split(" ")[1])
            i += 1

        if i > len(program) - 1:
            break

    if failed and not return_value:
        return -1
    else:
        return acc


def part1():
    return run(inputs, True)


def part2():
    for i in range(len(inputs)):
        if inputs[i].startswith("jmp"):
            program = inputs.copy()
            program[i] = inputs[i].replace("jmp", "nop")
            re = run(program)
            if re != -1:
                return re
        elif inputs[i].startswith("nop"):
            program = inputs.copy()
            program[i] = inputs[i].replace("jmp", "nop")
            re = run(program)
            if re != -1:
                return re


print(f"part 1 : {part1()}")
print(f"part 2 : {part2()}")
