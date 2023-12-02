from aoc_fetcher import get_data

input = get_data(2021, 7)

def part1():
    data = input.strip().split(",")
    data = [int(x) for x in data]
    #print(data[:5])
    min = sum(data) * sum(data)
    for crab in range(max(data)):
        new_min = 0
        for crab2 in data:
            n = abs(crab2 - crab)
            new_min += (n * n + n)/2
        if new_min < min:
            min = new_min
    print(min)

part1()
