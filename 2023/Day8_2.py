from aoc_fetcher import get_data
from functools import reduce

input = get_data(2023, 8).splitlines()
#input = open('Day8_test.txt', 'r').read().splitlines()

sequence = input[0]
sequence = sequence.replace('L', '0')
sequence = sequence.replace('R', '1')
temp = [line.split(' = ') for line in input[2::]]
step = {}
starters = []
for line in temp:
    if line[0][2] == 'A':
        starters.append(line[0])
    step[line[0]] = line[1][1:-1:].split(', ')
print(starters)

def check(nodes: [str]):
    return sum(list(map(lambda x: x[-1] == 'Z', nodes)))

def ggt(x, y):
    while y != 0:
        x,y = y, x%y
    return x

def kgv(x, y):
    return x * y / ggt(x, y)

minsteps = []
for starter in starters:
    count = 0
    idx = 0
    while(starter[2] != 'Z'):
        starter = step[starter][int(sequence[idx])]
        idx = (idx + 1)%(len(sequence))
        count+=1
    minsteps.append(count)
print(minsteps)
print(reduce(lambda x, y: kgv(x, y), minsteps, 1))