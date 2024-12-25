from aocd import data
import aoc_utils as au
import functools

#data = open('day22test.txt', 'r').read()
input = data.split('\n')

@functools.cache
def step(n):
    n1 = n * 64
    n = (n1 ^ n) % 16777216
    n2 = n // 32
    n = (n2 ^ n) % 16777216
    n3 = n * 2048
    n = (n3 ^ n) % 16777216
    return n

def getPrices(a, n):
    prices = [a % 10]
    for _ in range(n):
        a = step(a)
        prices.append(a % 10)
    return prices

def getChanges(prices):
    return [x[1] - x[0] for x in zip(prices[:-1], prices[1:])]

def part1():
    res = 0
    for secret in input:
        n = int(secret)
        for _ in range(2000):
            newN = step(n)
            n = newN
        res += n
    print(res)
    

def part2():
    prices = [getPrices(int(secret), 2000) for secret in input]
    changes = [getChanges(p) for p in prices]
    sequences = {}
    for i in range(len(input)):
        checkDuplicates = set()
        for j in range(len(changes[i])-3):
            sequence = tuple(changes[i][j:j+4])
            price = prices[i][j+4]
            if sequence not in checkDuplicates:
                au.add_to_num_dict(sequence, price, sequences)
                checkDuplicates.add(sequence)
    print(max(sequences.items(), key=lambda x : x[1]))

#part1()
part2()
