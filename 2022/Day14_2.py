from time import sleep

f = open('Day14_input.txt', 'r')

input = [[(int(point.split(',')[0]), int(point.split(',')[1])) for point in line.split(' -> ')] for line in f]

cave = []
for i in range(169):
    cave.append(['.'] * 700)

def printCave():
    sleep(0.1)
    for line in cave:
        print(''.join(line[460:520]))

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
cave[-1] = ['#'] * 700

source = (0,500)
cave[0][500] = '+'
sandPos = (0, 0)
units = 0
while(True):
    sandPosX = sandPos[1]
    sandPosY = sandPos[0]
    if (cave[sandPosY + 1][sandPosX] == '.'):
        sandPos = (sandPosY + 1, sandPosX)
    elif (cave[sandPosY + 1][sandPosX - 1] == '.'):
        sandPos = (sandPosY + 1, sandPosX - 1)
    elif (cave[sandPosY + 1][sandPosX + 1] == '.'):
        sandPos = (sandPosY + 1, sandPosX + 1)
    else:
        if (sandPos[0] == 0 and sandPos[1] == 500):
            break
        cave[sandPosY][sandPosX] = 'o'
        #if (sandPosY>100):
            #printCave()
        sandPos = (0, 500)
        units += 1

printCave()
print(units)
