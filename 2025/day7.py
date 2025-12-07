from aocd import get_data

DATA = open('day7.input').read()
DATA = get_data(day=7, year=2025)
INPUT = DATA.splitlines()
INPUT = [[c for c in line] for line in INPUT]

LOOKUP = [['.' for _ in range(len(INPUT[0]))] for _ in range(len(INPUT))]

s_index = INPUT[0].index('S')

def p1():
    row_size = 1
    res = 0
    INPUT[1][s_index] = '|'
    for row in range(2, len(INPUT)):
        for col in range(s_index - row_size, s_index + row_size + 1):
            if INPUT[row][col] == '^' and INPUT[row-1][col] == '|':
                INPUT[row][col-1] = '|'
                INPUT[row][col+1] = '|'
                res += 1
            if INPUT[row][col] == '.' and INPUT[row-1][col] == '|':
                INPUT[row][col] = '|'
        if row % 2 == 1:
            row_size += 1
    print(res)


def tachyon_step(ty, tx):
    if ty == len(INPUT) - 1:
        LOOKUP[ty][tx] = 1
        return 1
    if LOOKUP[ty][tx] != '.':
        return LOOKUP[ty][tx]
    if INPUT[ty][tx] == '^':
        left = tachyon_step(ty, tx-1)
        right = tachyon_step(ty, tx+1)
        LOOKUP[ty][tx] = left + right
        return left + right
    else:
        LOOKUP[ty][tx] = tachyon_step(ty+1, tx)
        return LOOKUP[ty][tx]


def p2():
    tachyon_step(1, s_index)
    print(LOOKUP[1][s_index])

#p1()
p2()