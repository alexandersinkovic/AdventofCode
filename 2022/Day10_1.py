from aoc_fetcher import get_data

input = get_data(2022, 10)
#f = open("Day10_test.txt", "r")

input = input.splitlines()
#input = [line[:-1:] for line in f]

counter = 1
cycle = 1

check = [20, 60, 100, 140, 180, 220]

result = 0

def checkCycle(cycle):
    if cycle in check:
        print(cycle, counter, cycle * counter)
        return cycle * counter
    return 0


for i in range(len(input)):
    parts = input[i].split(' ')
    result += checkCycle(cycle)
    if (parts[0] == 'noop'):
        cycle += 1
        continue
    if (parts[0] == 'addx'):
        cycle += 1
        result += checkCycle(cycle)
        cycle += 1
        counter += int(parts[1])
print(result)
