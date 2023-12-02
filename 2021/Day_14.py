from aoc_fetcher import get_data
from collections import defaultdict

input = get_data(2021, 14)


def part1():
    data = input.strip().splitlines()
    start = data[0]
    data = [line.split(" -> ") for line in data[2:]]
    print(start)

    count = defaultdict(lambda: 0)
    for char in [x for x in start]:
        count[char] += 1
    rules = {}
    for rule in data:
        rules[rule[0]] = rule[1]
    cur_pairs = defaultdict(lambda: 0)
    for i in range(len(start)-1):
        cur_pairs[start[i:i+2]] += 1
    #print(count)
    #print(rules)
    print(cur_pairs)

    for i in range(40):
        new_pairs = defaultdict(lambda: 0)
        #print("Begin of for:", cur_pairs)
        for key, val in cur_pairs.items():
            new_pair1 = key[0] + rules[key]
            new_pair2 = rules[key] + key[1]
            count[rules[key]] += val
            new_pairs[new_pair1] += val
            new_pairs[new_pair2] += val
        cur_pairs = new_pairs
    print(count)
    print(max(count.values()) - min(count.values()))

part1()
