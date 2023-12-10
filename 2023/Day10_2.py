from aoc_fetcher import get_data

input = get_data(2023, 10).splitlines()
#input = open('Day10_test.txt', 'r').read().splitlines()

pipemap = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], '7': [(0, -1), (1, 0)], 'F': [(1, 0), (0, 1)]}

starty = 0
startx = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            starty = i
            startx = j

check = [[-1 for j in range(len(input[0]))] for i in range(len(input))]
onlyloop = [['.' for j in range(len(input[0]))] for i in range(len(input))]
check[starty][startx] = 0
onlyloop[starty][startx] = '|'

def isconnected(sy, sx, dy, dx):
    pipe = input[dy][dx]
    if pipe == '.':
        return False
    connections = pipemap[pipe]
    for i in range(2):
        connection = connections[i]
        if dy + connection[0] == sy and dx + connection[1] == sx:
            return True
    return False

def findStartingDirections(sy, sx):
    res = []
    for i in range(-1, 2, 2):
        if isconnected(sy, sx, sy + i, sx):
            res.append((sy + i, sx))
        if isconnected(sy, sx, sy, sx + i):
            res.append((sy, sx + i))
    return res

directions = findStartingDirections(starty, startx)
y, x = directions[0]
goaly, goalx = directions[1]
check[y][x] = 1
onlyloop[y][x] = input[y][x]
counter = 1
while y != goaly or x != goalx:
    pipe = input[y][x]
    neighbors = pipemap[pipe]
    for neighbor in neighbors:
        if check[y+neighbor[0]][x+neighbor[1]] == -1:
            check[y+neighbor[0]][x+neighbor[1]] = counter+1
            onlyloop[y+neighbor[0]][x+neighbor[1]] = input[y+neighbor[0]][x+neighbor[1]]
            counter += 1
            y = y+neighbor[0]
            x = x+neighbor[1]
            break

tilesinside = 0
for line in onlyloop:
    outside = True
    i = 0
    while i < len(line):
        if line[i] == '.' and not outside:
            tilesinside += 1
            line[i] = 'X'
        if line[i] == '|':
            outside = not outside
        if line[i] == 'L':
            i += 1
            while(line[i] == '-'):
                i += 1
            if line[i] == '7':
                outside = not outside
        if line[i] == 'F':
            i += 1
            while(line[i] == '-'):
                i += 1
            if line[i] == 'J':
                outside = not outside
        i += 1
print(tilesinside)