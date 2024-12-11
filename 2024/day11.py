from aocd import data
from aoc_utils import add_to_num_dict
import time

#data = open('day11test.txt', 'r').read()
input = [int(x) for x in data.split(' ')]


def blinkStone(n, cache):
    if n in cache.keys():
        return cache[n]
    t = str(n)
    if len(t) % 2 == 0:
        add_to_num_dict(n, [int(t[:int(len(t)/2)]), int(t[int(len(t)/2):])], cache)
        return [int(t[:int(len(t)/2)]), int(t[int(len(t)/2):])]
    else:
        add_to_num_dict(n, [n * 2024], cache)
        return [n * 2024]

def blink(i, times):
    cache = {0: [1]}
    counters = {}
    for x in i:
        add_to_num_dict(x, 1, counters)
    for _ in range(times):
        new_Counters = {}
        for k,v in counters.items():
            r = blinkStone(k, cache)
            for n in r:
                add_to_num_dict(n, v, new_Counters)
        counters = new_Counters
    print(sum(counters.values()))

        
def p1(i):
    s_t = time.time()
    blink(i, 25)
    print(time.time() - s_t)

def p2(i):
    s_t = time.time()
    blink(i, 75)
    print(time.time() - s_t)

p1(input)
p2(input)