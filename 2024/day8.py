from aocd import data
from aoc_utils import splitTwice, add_to_list_dict

input = splitTwice(data)
boundx = len(input[0])
boundy = len(input)

antennas = {}
antinodes = []
for y in range(boundy):
    for x in range(boundx):
        if input[y][x] != '.':
            add_to_list_dict(input[y][x], (y, x), antennas)

def checkAntinode(ay, ax, by, bx):
    dy = ay - by
    dx = ax - bx
    if checkBounds(ay + dy, ax + dx):
        if (ay+dy, ax+dx) not in antinodes:
            antinodes.append((ay+dy, ax+dx))
    if checkBounds(by - dy, bx - dx):
        if (by-dy, bx-dx) not in antinodes:
            antinodes.append((by-dy, bx-dx))

def checkAntinodes(ay, ax, by, bx):
    dy = ay - by
    dx = ax - bx
    tggt = ggt(dy, dx)
    dy = dy / tggt
    dx = dx / tggt
    fx = ax
    fy = ay
    while(checkBounds(fy + dy, fx + dx)):
        if (fy+dy, fx+dx) not in antinodes:
            antinodes.append((fy+dy, fx+dx))
        fy = fy+dy
        fx = fx+dx
    fy = ay + dy
    fx = ax + dx
    while(checkBounds(fy - dy, fx - dx)):
        if (fy-dy, fx-dx) not in antinodes:
            antinodes.append((fy-dy, fx-dx))
        fy = fy-dy
        fx = fx-dx  

def checkBounds(y, x):
    return 0 <= y < boundy and 0 <= x < boundx

def ggt(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a

def part1():
    for antenna, coords in antennas.items():
        while(len(coords) > 0):
            curr = coords.pop(0)
            for coord in coords:
                checkAntinode(curr[0], curr[1], coord[0], coord[1])
    print(len(antinodes))

def part2():
    for antenna, coords in antennas.items():
        while(len(coords) > 0):
            curr = coords.pop(0)
            for coord in coords:
                checkAntinodes(curr[0], curr[1], coord[0], coord[1])
    print(len(antinodes))
part2()