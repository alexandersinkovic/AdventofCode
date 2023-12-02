from time import sleep

f = open('Day14_input.txt', 'r')

input = [[(int(point.split(',')[0])-440, int(point.split(',')[1])) for point in line.split(' -> ')] for line in f]

cave = []
for i in range(168):
    cave.append(['.'] * 110)

def printWholeCave():
    for line in cave:
        print(''.join(line))

def printCave(x, y):
    sleep(0.1)
    borderTop = y - 10
    borderBottom = y + 10
    if (y - 10 < 0):
        borderTop = 0
        borderBottom = 20
    if (y + 10 > 168):
        borderTop = 148
        borderBottom = 168
    for line in cave[borderTop:borderBottom:]:
        print(''.join(line[x-40:x+20:]))
    print('')

def motion(head, tail):
    if (head == tail):
        return head
    if (head < tail):
        return tail - 1
    else:
        return tail + 1

for wall in input:
    for i in range(1, len(wall)):
        head = wall[i]
        tail = wall[i-1]
        cave[tail[1]][tail[0]] = '#'
        while(head[0] != tail[0] or head[1] != tail[1]):
            tail = (motion(head[0], tail[0]), motion(head[1], tail[1]))
            cave[tail[1]][tail[0]] = '#'

source = (0,60)
cave[0][60] = '+'
sandPos = (1, 60)
units = 0
printWholeCave()
while(sandPos[0] != 167):
    sandPosX = sandPos[1]
    sandPosY = sandPos[0]
    printCave(sandPosX, sandPosY)
    cave[sandPosY][sandPosX] = '.'
    if (cave[sandPosY + 1][sandPosX] == '.'):
        sandPos = (sandPosY + 1, sandPosX)
        cave[sandPosY + 1][sandPosX] = 'o'
    elif (cave[sandPosY + 1][sandPosX - 1] == '.'):
        sandPos = (sandPosY + 1, sandPosX - 1)
        cave[sandPosY + 1][sandPosX - 1] = 'o'
    elif (cave[sandPosY + 1][sandPosX + 1] == '.'):
        sandPos = (sandPosY + 1, sandPosX + 1)
        cave[sandPosY + 1][sandPosX + 1] = 'o'
    else:
        cave[sandPosY][sandPosX] = 'o'
        sandPos = (1, 60)
        units += 1

printWholeCave()
print(units)
