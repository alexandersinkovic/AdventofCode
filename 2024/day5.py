from aocd import data
from aoc_utils import add_to_dict
from functools import cmp_to_key

#f = open('day5test.txt', 'r').read()
#data = f

rules, updates = data.split('\n\n')
rules = [rule.split('|') for rule in rules.splitlines()]
updates = [update.split(',') for update in updates.splitlines()]
rulesDict = {}
for before, after in rules:
    add_to_dict(int(before), int(after), rulesDict)

def myComparator(a, b):
    a = int(a)
    b = int(b)
    if b in rulesDict.keys() and a in rulesDict[b]:
        return 1
    elif a in rulesDict.keys() and b in rulesDict[a]:
        return -1
    return 0

def part1():
    res = 0
    for up in updates:
        if up == sorted(up, key=cmp_to_key(myComparator)):
            res += int(up[round((len(up)-1)/2)])
    print(res)

def part1Functional():
    return sum(map(lambda x : int(x[round((len(x)-1)/2)]),filter(lambda e : e == sorted(e, key=cmp_to_key(myComparator)), updates)))

def part2():
    res = 0
    for up in updates:
        if up != sorted(up, key=cmp_to_key(myComparator)):
            up = sorted(up, key=cmp_to_key(myComparator))
            res += int(up[round((len(up)-1)/2)])
    print(res)

part1()
print(part1Functional())
#part2()