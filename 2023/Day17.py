from aoc_fetcher import get_data

#input = get_data(2023, 17).splitlines()
input = open('Day17_test.txt', 'r').read().splitlines()

heatmap = input
leasthl = [[-1 for j in range(len(input[0]))] for i in range(len(input))]

def goStraight(dy, dx, y, x, s, hl):
    print(y, x)
    ny = y + dy
    if ny < 0 or ny >= len(input):
        return
    nx = x + dx
    if nx < 0 or nx >= len(input[0]):
        return
    nhl = hl + int(heatmap[ny][nx])
    if leasthl[ny][nx] == -1 or nhl < leasthl[ny][nx]:
        leasthl[ny][nx] = nhl
        turnLeft(ny - y, nx - x, ny, nx, nhl)
        if s < 3:
            goStraight(ny - y, nx - x, ny, nx, s + 1, nhl)
        turnRight(ny - y, nx - x, ny, nx, nhl)

def turnLeft(dy, dx, y, x, hl):
    print(y, x)  
    ny = y - dx
    if ny < 0 or ny >= len(input):
        return
    nx = x + dy
    if nx < 0 or nx >= len(input[0]):
        return
    nhl = hl + int(heatmap[ny][nx])
    if leasthl[ny][nx] == -1 or nhl < leasthl[ny][nx]:
        leasthl[ny][nx] = nhl
        turnLeft(ny - y, nx - x, ny, nx, nhl)
        goStraight(ny - y, nx - x, ny, nx, 1, nhl)
        turnRight(ny - y, nx - x, ny, nx, nhl)

def turnRight(dy, dx, y, x, hl):
    print(y, x)
    ny = y + dx
    if ny < 0 or ny >= len(input):
        return
    nx = x - dy
    if nx < 0 or nx >= len(input[0]):
        return
    nhl = hl + int(heatmap[ny][nx])
    if leasthl[ny][nx] == -1 or nhl < leasthl[ny][nx]:
        leasthl[ny][nx] = nhl
        turnLeft(ny - y, nx - x, ny, nx, nhl)
        goStraight(ny - y, nx - x, ny, nx, 1, nhl)
        turnRight(ny - y, nx - x, ny, nx, nhl)

goStraight(0, 1, 0, 1, 1, 0)
goStraight(1, 0, 1, 0, 1, 0)

for line in leasthl:
    print(line)

print(leasthl[-1][-1])