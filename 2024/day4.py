from aocd import data

f = open('day4test.txt', 'r').read()

def findXmas(field, y, x, dy, dx):
    #print(field[y])
    #print(field[y+dy][x+dx])
    #print(field[y+2*dy][x+2*dx])
    #print(field[y+3*dy][x+3*dx])
    if 0 <= x+3*dx < len(field[0]) and 0 <= y+3*dy < len(field):
        if field[y+dy][x+dx] == 'M' and field[y+(2*dy)][x+(2*dx)] == 'A' and field[y+(3*dy)][x+(3*dx)] == 'S':
            return True
    return False


def findX(field, y, x, dy, dx):
    if 0 <= x+dx < len(field[0]) and 0 <= y+dy < len(field) and 0 <= x-dx < len(field[0]) and 0 <= y-dy < len(field):
        if field[y+dy][x+dx] in ('M', 'S') and field[y-dy][x+dx] in ('M', 'S') and field[y-dy][x-dx] in ('M', 'S') and field[y+dy][x-dx] in ('M', 'S') and field[y+dy][x+dx] != field[y-dy][x-dx] and field[y-dy][x+dx] != field[y+dy][x-dx]:
            return True
    return False


def part1(input):
    count = 0
    input = [[c for c in line] for line in input.split('\n')]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'X':
                for dy in range (-1, 2, 2):
                    for dx in range(-1, 2, 2):
                        if findXmas(input, y, x, dy, dx):
                            #print(y, x, dy, dx)
                            count += 1
    print(count)

def part2(input):
    count = 0
    input = [[c for c in line] for line in input.split('\n')]
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'A':
                for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if findX(input, y, x, dy, dx):
                        #print(y, x, dy, dx)
                        count += 1
                        break
    print(count)
    

#findXmas([[c for c in line] for line in f.split('\n')], 0, 4, 1, 1)
#part1(f)
#part1(data)
#part2(f)
part2(data)