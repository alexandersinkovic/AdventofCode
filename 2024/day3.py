#from aoc_fetcher import get_data
from aocd import data
import re

#input = get_data(2024, 3).splitlines()

def part1(input):
    input = [re.findall(r'mul\([0-9]+,[0-9]+\)', line) for line in input]
    res = 0
    for line in input:
        for mul in line:
            a, b = mul[4:-1].split(',')
            res += int(a) * int(b)
    print(res)

def part2(input):
    input = [re.findall(r'do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\)', line) for line in input]
    res = 0
    do = True
    for line in input:
        for op in line:
            if op == 'do()':
                do = True
            elif op == "don't()":
                do = False
            elif op[0] == 'm' and do:
                a, b = op[4:-1].split(',')
                res += int(a) * int(b)
    print(res)

#part1(input)
#part2(input)
print(data)