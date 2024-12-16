from heapq import heappush, heappop
from aocd import data
from aoc_utils import splitTwice, DIRS4, TURNLEFT, TURNRIGHT

#data = open('day16test.txt', 'r').read()
f = open('day16out.txt', 'w')
input = splitTwice(data)
distMap = [[['.' for _ in range(4)] for _ in l] for l in input]
DIRS4Translate = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def flood(y, x, dir, points, ey, ex):
    checkSteps = [(points, y, x, dir)]
    while(len(checkSteps) > 0):
        cpoints, cy, cx, cdir = heappop(checkSteps)
        #print(cy, cx, cdir, cpoints)
        #print(cy, cx, cpoints)
        #print(distMap[ey][ex])
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
        if distMap[ey][ex][0] != '.' and distMap[ey][ex][0] < 108000:
            f.write(','.join([str(cy), str(cx), dir, str(cpoints)]))
            for line in distMap:
                ml = [str(c) for c in line]
                for i in range(len(line)):
                    if line[i] == '.':
                        ml[i] = '.......'
                    else:
                        ml[i] = ml[i].zfill(6) + ' '
                f.write(''.join(ml) + '\n')
            print('')
            f.write('\n')

def calcDist(y, x, ey, ex):
    dy = abs(y - ey)
    dx = abs(x - ex)
    return dy+dx

def part1():
    ry, rx = [0, 0]
    ey, ex = [0, 0]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                ry, rx = y, x
            if input[y][x] == 'E':
                ey, ex = y, x
    print(ry, rx, ey, ex)
    flood(ry, rx, 'R', 0, ey, ex)
    print(distMap[ey][ex][0])

part1()
#107476 is too high
#107475 is too high