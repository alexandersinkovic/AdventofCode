from aoc_fetcher import get_data

input = get_data(2022, 10)
#f = open("Day10_test.txt", "r")

input = input.splitlines()
#input = [line[:-1:] for line in f]

counter = 1
cycle = 0

check = [20, 60, 100, 140, 180, 220]

result = []
for i in range(6):
    result.append(['.'] * 40)

def checkCycle(counter, x):
    if counter - 1 <= x and x <= counter + 1:
        return '#'
    return '.'


for i in range(len(input)):
    y = int(cycle / 40)
    x = cycle % 40
    parts = input[i].split(' ')
    result[y][x] = checkCycle(counter, x)
    if (parts[0] == 'noop'):
        cycle += 1
        continue
    if (parts[0] == 'addx'):
        cycle += 1
        y = int(cycle / 40)
        x = cycle % 40
        result[y][x] = checkCycle(counter, x)
        cycle += 1
        counter += int(parts[1])
for line in result:
    print(''.join(line))
