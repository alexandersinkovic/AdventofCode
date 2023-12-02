from aoc_fetcher import get_data

input = get_data(2022, 5)

input = input.splitlines()

crates = {  '1': ['B', 'Z', 'T'],
            '2': ['V', 'H', 'T', 'D', 'N'],
            '3': ['B', 'F', 'M', 'D'],
            '4': ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
            '5': ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
            '6': ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
            '7': ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
            '8': ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
            '9': ['M', 'Q', 'L', 'F', 'D', 'S']
}

input = input[10::]
for line in input:
    parts = line.split(' from ')
    moves = parts[0][5::]
    [target, destination] = parts[1].split(' to ')
    for i in range(0, int(moves)):
        elem = crates[target].pop()
        crates[destination].append(elem)

result = ''
for i in range(1, 10):
    result += crates[str(i)].pop()

print(result)
