import fileinput

inputs = []

for li in fileinput.input("input.txt"):
    inputs.append(li)


def count_around(current_state, line, column):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == i == 0:
                continue
            if 0 <= line + i < len(current_state):
                if 0 <= column + j < len(current_state[line + i]):
                    if current_state[line + i][column + j] == '#':
                        c += 1
    return c


def count_around_2(current_state, line, column):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == i == 0:
                continue
            distance = 1
            s_line = line + i * distance
            s_column = column + j * distance
            while 0 <= line + i * distance < len(current_state) and 0 <= column + j * distance < len(current_state[s_line]):
                if current_state[s_line][s_column] == '#':
                    c += 1
                    break
                elif current_state[s_line][s_column] == 'L':
                    break
                distance += 1
                s_line = line + i * distance
                s_column = column + j * distance
    return c


def print_state(current_state):
    for line in current_state:
        print(*line)


def gen_result(current_state, count_function, min_around):
    count = 0
    changes = 1
    while changes != 0:
        current_state, changes = game_of_seats(current_state, count_function, min_around)
        count += 1

    count_occupied = 0

    for line in current_state:
        for seat in line:
            if seat == '#':
                count_occupied += 1
    return count_occupied


def game_of_seats(current_state, count_function, min_around):
    new_state = []
    changes = 0
    for line in range(len(current_state)):
        new_state.append([])
        for column in range(len(current_state[line])):
            seat = current_state[line][column]
            if seat == '.':
                new_state[line].append('.')
            elif seat == 'L':
                if count_function(current_state, line, column) == 0:
                    new_state[line].append('#')
                    changes += 1
                else:
                    new_state[line].append('L')
            elif seat == '#':
                if count_function(current_state, line, column) >= min_around:
                    new_state[line].append('L')
                    changes += 1
                else:
                    new_state[line].append('#')
    return new_state, changes


def part1():
    return gen_result(inputs, count_around, 4)


def part2():
    return gen_result(inputs, count_around_2, 5)


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
