from aocd import data
from aoc_utils import getIntFromString
import re

#data = open('day14test.txt', 'r').read()
robots = data.split('\n')
Y = 103
YM = 51
X = 101
XM = 50
SECONDS = 100

def part1():
    q = [0,0,0,0]
    for robot in robots:
        rx, ry, vx, vy = getIntFromString(robot)

        ry = (ry + vy * SECONDS) % Y
        rx = (rx + vx * SECONDS) % X

        if ry != YM and rx != XM:
            if ry > YM:
                if rx > XM:
                    q[3] += 1
                else:
                    q[2] += 1
            else:
                if rx > XM:
                    q[1] += 1
                else: 
                    q[0] += 1
    print(q[0], q[1], q[2], q[3])
    print(q[0] * q[1] * q[2] * q[3])

def part2():
    for ridx in range(len(robots)):
        rx, ry, vx, vy = getIntFromString(robots[ridx])
        robots[ridx] = [ry, rx, vy, vx]
            
    for s in range(1, SECONDS*100 + 1):
        if s % 1000 == 0:
            print('Simulating Second', s)
        bath = [['.' for _ in range(X)] for _ in range(Y)]
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % Y
            robot[1] = (robot[1] + robot[3]) % X

            bath[robot[0]][robot[1]] = '#'
        giantString = ''.join([''.join(l) for l in bath])
        if re.search(r'########', giantString) is not None:
            print(s)
            for line in bath:
                print(''.join(line))
            break
        
part1()
part2()