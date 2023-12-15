from aoc_fetcher import get_data
from functools import reduce
from collections import defaultdict

input = get_data(2023, 15).splitlines()[0]
#input = open('Day15_test.txt', 'r').read()

def hash(s):
    return reduce(lambda x, y: ((x + ord(y))*17)%256, s, 0 )

def part1(seq: str):
    sequence = sum(map(lambda c: hash(c) , seq.split(',')))
    print(sequence)

def myRemove(seq: [(str, str)], label):
    return [s for s in seq if s[0] != label]

def myContains(seq, label):
    for i in range(len(seq)):
        if seq[i][0] == label:
            return i
    return -1

def defaultValue():
    return []

def part2(seq: str):
    boxes = defaultdict(defaultValue)
    lenses = seq.split(',')
    for lense in lenses:
        if lense[-1] == '-':
            label = lense[:len(lense)-1]
            boxes[hash(label)] = myRemove(boxes[hash(label)], label)
        else:
            label = lense[:-2]
            idx = myContains(boxes[hash(label)], label)
            if idx == -1:   
                boxes[hash(label)].append((label, lense[-1]))
            else:
                boxes[hash(label)][idx] = (label, lense[-1])
    return sum([(1 + idx) * sum([int(l[1]) * (i+1) for i, l in enumerate(b)]) for idx, b in boxes.items()])

print(part2(input))