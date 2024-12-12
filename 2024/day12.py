from aocd import data
from aoc_utils import splitTwice, DIRS_ADJ, add_to_num_dict
import re

#data = open('day12test.txt', 'r').read()
oneLine = data.replace('\n', '')
input = splitTwice(data)
inputPad = [['0'] * (len(input[0])+ 2)]
for line in input:
    f = ['0']
    f.extend(line)
    f.extend(['0'])
    inputPad.append(f)
inputPad.append(['0'] * (len(input[0])+ 2))
visitedRegions = [[0 for _ in line] for line in inputPad]
for y in range(len(visitedRegions)):
    for x in range(len(visitedRegions[0])):
        if x == 0 or x == len(visitedRegions)-1 or y == 0 or y == len(visitedRegions[0])-1:
            visitedRegions[y][x] = 1

regions = []

def floodFill(y, x, k, a, p):
    if visitedRegions[y][x] == 0:
        visitedRegions[y][x] = 1
        for dy, dx in DIRS_ADJ:
            if 0 <= y+dy < len(input) and 0 <= x+dx < len(input[0]):
                if input[y+dy][x+dx] == k:
                    a, p  = floodFill(y+dy, x+dx, k, a, p)
                else:
                    p+=1
            else:
                p+= 1
        a+= 1
    return a, p


def floodFillRegions(y, x, k, a, p:set[list[int]]):
    if visitedRegions[y][x] == 0:
        visitedRegions[y][x] = 1
        isPerimeter = False
        for dy, dx in DIRS_ADJ:
            if inputPad[y+dy][x+dx] == k:
                a, p  = floodFillRegions(y+dy, x+dx, k, a, p)
            else:
                isPerimeter = True
        if isPerimeter:
            p.add((y, x))
        a+= 1
    return a, p


def calcSides(k, perimeter):
    yCoords = set(map(lambda x: x[0], perimeter))
    ySides = 0
    for y in yCoords:
        xBelow = []
        xAbove = []
        for py, px in perimeter:
            if py == y:
                if inputPad[py-1][px] != k:
                    xAbove.append(px)
                if inputPad[py+1][px] != k:
                    xBelow.append(px)
        xBelow.sort()
        xAbove.sort()
        if len(xBelow) > 0:
            for i in range(len(xBelow)-1):
                if xBelow[i]+1 != xBelow[i+1]:
                    ySides += 1
            ySides += 1
        if len(xAbove) > 0:
            for i in range(len(xAbove)-1):
                if xAbove[i]+1 != xAbove[i+1]:
                    ySides += 1
            ySides += 1
    #whole XCoords Thing is probably useless. Just return ySides * 2
    # DELETE -------------------
    xCoords = set(map(lambda x: x[1], perimeter))
    xSides = 0
    for x in xCoords:
        yBelow = []
        yAbove = []
        for py, px in perimeter:
            if px == x:
                if inputPad[py][px-1] != k:
                    yAbove.append(py)
                if inputPad[py][px+1] != k:
                    yBelow.append(py)
        yBelow.sort()
        yAbove.sort()
        if len(yBelow) > 0:
            for i in range(len(yBelow)-1):
                if yBelow[i]+1 != yBelow[i+1]:
                    xSides += 1
            xSides += 1
        if len(yAbove) > 0:
            for i in range(len(yAbove)-1):
                if yAbove[i]+1 != yAbove[i+1]:
                    xSides += 1
            xSides += 1
    #End of DELETE ----------------
    #return ySides * 2
    return xSides + ySides


def part1():
    res = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if visitedRegions[y][x] == 0:
                area, perimeter = floodFill(y, x, input[y][x], 0, 0)
                regions.append((area, perimeter))
                res += area * perimeter
    print(res)

def part2():
    res = 0
    for y in range(1, len(inputPad)-1):
        for x in range(1, len(inputPad[0])-1):
            if visitedRegions[y][x] == 0:
                area, perimeter = floodFillRegions(y, x, inputPad[y][x], 0, set())
                sides = calcSides(inputPad[y][x], perimeter)
                res += area * sides
    print(res)
#part1()
part2()
