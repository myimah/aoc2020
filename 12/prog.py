import fileinput
from math import floor, cos, sin, radians

inputs = []

for line in fileinput.input("input.txt"):
    if line == '\n':
        continue
    inputs.append(line.replace("\n", ""))


def part1():
    pos_north = 0
    pos_east = 0
    directions = ["N", "E", "S", "W"]
    facing = 1

    for move in inputs:
        direc = move[:1]
        length = int(move[1:])

        if direc == "F":
            direc = directions[facing % len(directions)]

        if direc == "N":
            pos_north += length
        if direc == "S":
            pos_north -= length
        if direc == "E":
            pos_east += length
        if direc == "W":
            pos_east -= length
        if direc == "R":
            facing += floor(length / 90)
        if direc == "L":
            facing -= floor(length / 90)

    return abs(pos_east) + abs(pos_north)

def rotate(point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = (0, 0)
    px, py = point

    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
    return round(qx), round(qy)


def part2():
    pos_north = 0
    pos_east = 0
    waypoint_north = 1
    waypoint_east = 10

    for move in inputs:
        direc = move[:1]
        length = int(move[1:])

        if direc == "F":
            pos_north += length * waypoint_north
            pos_east += length * waypoint_east
        elif direc == "R":
            waypoint_east, waypoint_north = rotate((waypoint_east, waypoint_north), -radians(length))
        elif direc == "L":
            waypoint_east, waypoint_north = rotate((waypoint_east, waypoint_north), radians(length))
        elif direc == "N":
            waypoint_north += length
        elif direc == "S":
            waypoint_north -= length
        elif direc == "E":
            waypoint_east += length
        elif direc == "W":
            waypoint_east -= length

    return abs(pos_east) + abs(pos_north)


print(f"Part 1 : {part1()}")
print(f"Part 2 : {part2()}")
