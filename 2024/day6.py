from aocd import data
from aoc_utils import splitTwice
import time

#f = open('day6test.txt', 'r').read()
#data = f

DIRS4 = {'W': (0, -1), 'S': (1, 0), 'E': (0, 1), 'N': (-1, 0)}
ROTATE = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

def getGuardPosition(input: list[list[str]]):
    for y in range(len(input)):
        if '^' in input[y]:
            return (y, input[y].index('^'))
        
def step(y, x, dir, input, visited):
    dy, dx = DIRS4[dir]
    if isBlocked(y+dy, x+dx, input):
        dir = rotate(dir)
        return y, x, dir
    visited[y][x] = 'X'
    return y + dy, x + dx, dir

def step2(y, x, dir, input, visited, visitedDir):
    dy, dx = DIRS4[dir]
    if isBlocked(y+dy, x+dx, input):
        dir = rotate(dir)
        return y, x, dir
    visited[y][x] = 'X'
    visitedDir[y][x].append(dir)
    return y + dy, x + dx, dir

def isBlocked(y, x, input):
    if 0 <= y < len(input) and 0 <= x < len(input[0]):
        return input[y][x] == '#'
    return False

def rotate(dir):
    return ROTATE[dir]

def loopFound(y, x, dir, visitedDir):
    return dir in visitedDir[y][x]

def part1():
    input = splitTwice(data)
    visited = [[x for x in line] for line in data.split('\n')]
    y, x = getGuardPosition(input)
    dir = 'N'
    while 0 <= y < len(input) and 0 <= x < len(input[0]):
        y, x, dir = step(y, x, dir, input, visited)
    return visited


def part2():
    start_time = time.time()
    input = splitTwice(data)
    res = 0
    path = part1()
    for oy in range(len(input)):
        for ox in range(len(input[0])):
            if path[oy][ox] == 'X':
                y, x = getGuardPosition(input)
                dir = 'N'
                visited = [[x for x in line] for line in data.split('\n')]
                visitedDir = [[[] for x in line] for line in data.split('\n')]
                if (oy == y and ox == x) or input[oy][ox] == '#':
                    continue
                input[oy][ox] = '#'
                while 0 <= y < len(input) and 0 <= x < len(input[0]):
                    if loopFound(y, x, dir, visitedDir):
                        res += 1
                        break
                    y, x, dir = step2(y, x, dir, input, visited, visitedDir)
                input[oy][ox] = '.'
    print(res)
    print(time.time() - start_time)

#part1()
#print(sum(map(lambda x: len(list(filter(lambda f: f == 'X', x))), part1())))
part2()