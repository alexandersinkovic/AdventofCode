from heapq import heappush, heappop
from aocd import data
from aoc_utils import splitTwice, DIRS4, TURNLEFT, TURNRIGHT, printMatrix

#data = open('day16test.txt', 'r').read()
#f = open('day16out.txt', 'w')
input = splitTwice(data)
distMap = [[['.' for _ in range(4)] for _ in l] for l in input]
DIRS4Translate = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
DIRINVERSE = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

def flood(y, x, dir, points, ey, ex):
    checkSteps = [(points, y, x, dir)]
    while(len(checkSteps) > 0):
        cpoints, cy, cx, cdir = heappop(checkSteps)
        if distMap[cy][cx][DIRS4Translate[cdir]] == '.' or cpoints < distMap[cy][cx][DIRS4Translate[cdir]]:
            distMap[cy][cx][DIRS4Translate[cdir]] = cpoints
            if input[cy][cx] == 'E':
                continue
            # forward
            dy, dx = DIRS4[cdir]
            if input[cy+dy][cx+dx] != '#':
                heappush(checkSteps, (cpoints+1, cy+dy, cx+dx, cdir))
            # left turn
            dy, dx = DIRS4[TURNLEFT[cdir]]
            if input[cy+dy][cx+dx] != '#':
                heappush(checkSteps, (cpoints+1001, cy+dy, cx+dx, TURNLEFT[cdir]))
            # right turn
            dy, dx = DIRS4[TURNRIGHT[cdir]]
            if input[cy+dy][cx+dx] != '#':
                heappush(checkSteps, (cpoints+1001, cy+dy, cx+dx, TURNRIGHT[cdir]))
        if distMap[ey][ex][0] != '.':
            checkSteps = list(filter(lambda s: s[0] < distMap[ey][ex][0], checkSteps))

def part1():
    ry, rx = [0, 0]
    ey, ex = [0, 0]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                ry, rx = y, x
            if input[y][x] == 'E':
                ey, ex = y, x
    flood(ry, rx, 'R', 0, ey, ex)
    print(distMap[ey][ex][0])

def part2():
    ey, ex = [0, 0]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'E':
                ey, ex = y, x
    score = [d for d in distMap[ey][ex] if d != '.'][0]
    step = [(ey, ex, 'D')]
    output = [['.' for _ in l] for l in input]
    while len(step) > 0:
        nextStep = set()
        for sy, sx, sdir in step:
            score = distMap[sy][sx][DIRS4Translate[DIRINVERSE[sdir]]]
            dy, dx = DIRS4[sdir]
            if score - 1 == distMap[sy+dy][sx+dx][DIRS4Translate[DIRINVERSE[sdir]]]:
                nextStep.add((sy+dy, sx+dx, sdir))
            #dy, dx = DIRS4[TURNLEFT[sdir]]
            if score - 1001 == distMap[sy+dy][sx+dx][DIRS4Translate[TURNRIGHT[sdir]]]:
                nextStep.add((sy+dy, sx+dx, TURNLEFT[sdir]))
            #dy, dx = DIRS4[TURNRIGHT[sdir]]
            if score - 1001 == distMap[sy+dy][sx+dx][DIRS4Translate[TURNLEFT[sdir]]]:
                nextStep.add((sy+dy, sx+dx, TURNRIGHT[sdir]))
        for sy, sx, sd in list(nextStep):
            output[sy][sx] = sd
        step = list(nextStep)
    printMatrix(output)
    count = 1
    for line in output:
        for c in line:
            if c != '.':
                count += 1
    print(count)


part1()
# part2 can only run after part1
part2()