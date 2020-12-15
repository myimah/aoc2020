from math import ceil

numbers = []
with open("input.txt", "r") as fi:
    numbers = fi.readlines()


def input_clean():
    mp = []
    for x in numbers:
        x = x.rstrip("\n")
        mp.append(x)
    return mp


number = input_clean()
initM = 127

result = 0
deuxR = 0
initB = 0
initMS = 7
initBS = 0
intersec1 = 63
intersec2 = 4
for x in number:
    for i in x:
        if i == 'F':
            initM = initM - intersec1
            intersec1 = int(intersec1 / 2)
        elif i == 'B':
            initB = ceil(initB + intersec1)
            intersec1 = int(intersec1 / 2)
        elif i == 'R':
            initBS = ceil(initBS + intersec2)
            intersec2 = int(intersec2 / 2)
        elif i == 'L':
            initMS = initMS - intersec2
            intersec2 = int(intersec2 / 2)
    result = initM * 8 + initBS
    if result >= deuxR:
        deuxR = result
print(deuxR)
