import fileinput

inputs = []

for line in fileinput.input("input.txt"):
    inputs.append(line)

numbers = [int(i) for i in inputs[0].split(",")]


def game(nth=2020):
    numbers_copy = numbers.copy()
    most_recent = {}
    for i in range(len(numbers_copy)):
        most_recent[numbers_copy[i]] = i

    for i in range(len(numbers) - 1, nth - 1):
        current_number = numbers_copy[i]
        if current_number in most_recent.keys():
            numbers_copy.append(i - most_recent[current_number])
            most_recent[current_number] = i
        else:
            numbers_copy.append(0)
            most_recent[current_number] = i

    return numbers_copy[-1]


def part1():
    return game()


def part2():
    return game(30000000)


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
