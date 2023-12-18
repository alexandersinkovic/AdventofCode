#from aoc_fetcher import get_data

#input = get_data(2023, 18).splitlines()
input = open("Day18_in.txt", 'r').read().splitlines()
#input = open("Day18_test.txt", 'r').read().splitlines()

steps = [x.split(' ')[:2] for x in input]
directions = {'R': (0, 1), 'L': (0,-1), 'U': (-1, 0), 'D': (1, 0)}
fieldSize = 800

lava_pit = [['.' for y in range(fieldSize)] for x in range(fieldSize)]
sx = int(fieldSize/2)
sy = int(fieldSize/2)

def calcLava(pit):
    res = 0
    for line in pit:
        counting = False
        for i in range(len(line)):
            if line[i] == '#':
                counting = not counting
                res += 1
            elif counting:
                res += 1
    return res

def floodFill(y, x):
    queue = [(y, x)]
    lava_pit[y][x] = '#'
    while queue:
        my, mx = queue.pop()
        newcoords = [(my-1, mx), (my+1, mx), (my, mx-1), (my, mx+1)]
        for cy, cx in newcoords:
            if lava_pit[cy][cx] == '.':
                lava_pit[cy][cx] = '#'
                queue.append((cy, cx))

for d, s in steps:
    dy = directions[d][0] * 1
    dx = directions[d][1] * 1
    for i in range(int(s)):
        sx = sx + dx
        sy = sy + dy
        #print(sy, sx)
        lava_pit[sy][sx] = '#'

#print(calcLava(lava_pit))

floodFill(470, 560)

#f = open("Day18_out.txt", 'a')

#for line in lava_pit:
#    f.write(''.join(line) + '\n')
count = 0
for line in lava_pit:
    for c in line:
        if c == '#':
            count += 1

print(count)