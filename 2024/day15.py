from aocd import data
from aoc_utils import splitTwice, DIRS4
import time

TRANSLATE = {'<': 'L', 'v': 'D', '>': 'R', '^': 'U'}
BLOAT = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
BOX = {'[': 1, ']': -1}


#data = open('day15test.txt', 'r').read()
warehouse, movement = data.split('\n\n')
warehouse = splitTwice(warehouse)
biggerWarehouse = [[BLOAT[c] for c in l] for l in warehouse]
biggerWarehouse = [[c for c in ''.join(l)] for l in biggerWarehouse]
movement = ''.join(movement.split('\n'))

def move(ry, rx, dy, dx):
    #print('move', ry, rx, dy, dx)
    boxes = []
    tx = rx
    ty = ry
    while warehouse[ty+dy][tx+dx] == 'O':
        boxes.append([ty+dy, tx+dx])
        ty += dy
        tx += dx
    if warehouse[ty+dy][tx+dx] == '#':
        return ry, rx
    else:
        #print(boxes)
        if len(boxes) > 0:
            by, bx = boxes[-1]
            by += dy
            bx += dx
            warehouse[by][bx] = 'O'
        warehouse[ry+dy][rx+dx] = '@'
        warehouse[ry][rx] = '.'
    return ry +dy, rx + dx


def gpsSum(warehouse, id):
    res = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[0])):
            if warehouse[y][x] == id:
                res += y * 100 + x
    return res


def part1():
    robot = [0,0]
    for x in range(len(warehouse)):
        if '@' in warehouse[x]:
            robot = [x, warehouse[x].index('@')]
    #print(robot)
    moves = [m for m in movement]
    for i in range(len(moves)):
        #print(moves[i])
        dy, dx = DIRS4[TRANSLATE[moves[i]]]
        #print(dy, dx)
        robot = move(robot[0], robot[1], dy, dx)
        #for l in warehouse:
        #    print(''.join(l))
    print(gpsSum(warehouse, 'O'))

def move2(ry, rx, dy, dx):
    #print('move', ry, rx, dy, dx)
    if biggerWarehouse[ry+dy][rx+dx] == '#':
        return ry, rx
    elif biggerWarehouse[ry+dy][rx+dx] == '.':
        biggerWarehouse[ry+dy][rx+dx] = '@'
        biggerWarehouse[ry][rx] = '.'
        return ry+dy, rx+dx
    else: 
        boxes = []
        moreBoxes = True
        bx = BOX[biggerWarehouse[ry+dy][rx+dx]]
        boxes.append([(ry+dy, rx+dx),(ry+dy, rx+dx+bx)])
        while moreBoxes:
            #print(boxes)
            moreBoxes = False
            currBoxes = boxes[-1]
            nextBoxes = set()
            for by, bx in currBoxes:
                if biggerWarehouse[by+dy][bx+dx] in ['[', ']']:
                    if ((by+dy, bx+dx) not in currBoxes):
                        moreBoxes = True
                        nextBoxes.add((by+dy, bx+dx))
                        nextBoxes.add((by+dy, bx+dx+BOX[biggerWarehouse[by+dy][bx+dx]]))
                elif biggerWarehouse[by+dy][bx+dx] == '#':
                    return ry, rx
            boxes.append(list(nextBoxes))

        biggerWarehouseCopy = [[c for c in l] for l in biggerWarehouse]
        boxes.reverse()
        for translateBoxes in boxes:
            #print('Push boxes:', translateBoxes)
            for by, bx in translateBoxes:
                #print(by, bx)
                #print(biggerWarehouse[by+dy][bx+dx])
                #print(biggerWarehouseCopy[by][bx])
                biggerWarehouse[by+dy][bx+dx] = biggerWarehouseCopy[by][bx]
                if dx == 0:
                    biggerWarehouse[by][bx] = '.'

    
        biggerWarehouse[ry+dy][rx+dx] = '@'
        biggerWarehouse[ry][rx] = '.'
    return ry +dy, rx + dx

def part2():
    robot = [0,0]
    
    #for l in biggerWarehouse:
    #    print(''.join(l))
    for x in range(len(biggerWarehouse)):
        if '@' in biggerWarehouse[x]:
            robot = [x, biggerWarehouse[x].index('@')]
    moves = [m for m in movement]
    for i in range(len(moves)):
        #print(moves[i])
        dy, dx = DIRS4[TRANSLATE[moves[i]]]
        #print(dy, dx)
        robot = move2(robot[0], robot[1], dy, dx)
        #for l in biggerWarehouse:
        #    print(''.join(l))
    print(gpsSum(biggerWarehouse, '['))

s_t = time.time()
part1()
print(time.time()-s_t)
s_t = time.time()
part2()
print(time.time()-s_t)
