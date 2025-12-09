from aocd import get_data

DATA = get_data(day=9, year=2025)
DATA = open('day9.input').read()
INPUT = DATA.splitlines()
COORDS = [list(map(int, c.split(','))) for c in INPUT]
MAX_X = max([c[1] for c in COORDS]) + 1
MAX_Y = max([c[0] for c in COORDS]) + 1

def get_square_size(y1, x1, y2, x2):
    return abs(y1 - y2 + 1) * abs(x1 - x2 + 1)

def check_square(y1, x1, y2, x2):
    pass

def get_grid():
    return [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]

def fill_vertical(grid, y1, y2, x):
    direction = 1 if y2 >= y1 else -1
    for y in range(y1, y2 + direction, direction):
        grid[y][x] = 1

def fill_horizontal(grid, x1, x2, y):
    direction = 1 if x2 >= x1 else -1
    for x in range(x1, x2 + direction, direction):
        grid[y][x] = 1

def p1():
    squares = []
    for idx1 in range(len(COORDS)):
        for idx2 in range(idx1+1, len(COORDS)):
            y1, x1 = COORDS[idx1]
            y2, x2 = COORDS[idx2]
            squares.append(get_square_size(y1, x1, y2, x2))
    print(max(squares))

def p2():
    grid = get_grid()
    prev_y, prev_x = COORDS[0]
    grid[prev_y][prev_x] = 1
    COORDS.append(COORDS[0])
    #Draw Bounds
    for y,x in COORDS[1:]:
        print(y, x)
        if x == prev_x:
            fill_vertical(grid, prev_y, y, x)
        else:
            fill_horizontal(grid, prev_x, x, y)
        prev_x = x
        prev_y = y
    
    #Fill Loop
    for row in grid:
        is_inside = False
        for y in row:
            if y == 1 and is_inside:
                pass


#p1()
# 4744762064 not right
p2()