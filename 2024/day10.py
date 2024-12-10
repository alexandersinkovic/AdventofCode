from aocd import data
from aoc_utils import splitTwice, DIRS4

#data = open('day10test.txt', 'r').read()
input = splitTwice(data)
input = [[int(x) for x in l] for l in input]

def r(y, x, s, reached):
    res = 0
    if s == 9:# and (y, x) not in reached: #Comment is for part1
        reached.append((y, x))
        return 1
    for dy, dx in DIRS4:
        if 0<=y+dy < len(input) and 0<=x+dx<len(input[0])and input[dy+y][dx+x] == s+1:
            res += r(dy+y, dx+x, s+1, reached)
    return res


def part1():
    res = 0
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 0:
                res += r(y, x, 0, [])
    print(res)

part1()